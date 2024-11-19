from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import requests
import psycopg2
import os
import time

default_args = {
    'owner': 'airflow',
    'retries': 5,
    'retry_delay': timedelta(minutes=5),
}

# This function ensures the requests adhere to the rate limits
def fetch_and_store_food_data(**kwargs):
    USDA_API_KEY = os.getenv("USDA_API_KEY")
    page = 1
    page_size = 200  # Adjust based on your needs
    rate_limit = 1000  # 1000 requests per hour
    request_interval = 3600 / rate_limit  # 3.6 seconds between requests

    db_name = os.getenv("USDA_DB_NAME")
    db_user = os.getenv("USDA_DB_AIRFLOW_USER")
    db_password = os.getenv("USDA_DB_AIRFLOW_PASSWORD")
    db_host = os.getenv("USDA_DB_HOST")
    db_port = os.getenv("USDA_DB_PORT")

    while True:
        url = f"https://api.nal.usda.gov/fdc/v1/foods/list?api_key={USDA_API_KEY}&pageSize={page_size}&pageNumber={page}"
        response = requests.get(url)
        
        # Check for rate limiting or API issues
        if response.status_code == 429:
            # If we hit a rate limit, log it and break out
            print("Rate limit reached. Stopping requests.")
            break
        
        data = response.json()

        if not data:
            break  # Stop if no more data

        # Connect to your Postgres database using environment variables
        conn = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        cursor = conn.cursor()

        for food in data:
            # Check if food is a dictionary, otherwise log it
            if isinstance(food, dict):
                # Collect all the necessary fields (including optional ones)
                fdc_id = food['fdcId']
                description = food['description']
                data_type = food['dataType']
                publication_date = food.get('publicationDate')
                brand_owner = food.get('brandOwner')
                gtin_upc = food.get('gtinUpc')
                ndb_number = food.get('ndbNumber')
                food_code = food.get('foodCode')

                # Insert food data
                cursor.execute("""
                    INSERT INTO food (fdc_id, description, data_type, publication_date, brand_owner, gtin_upc, ndb_number, food_code)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (fdc_id) DO NOTHING;
                """, (fdc_id, description, data_type, publication_date, brand_owner, gtin_upc, ndb_number, food_code))

                # Get the food_id from the food table (whether newly inserted or existing)
                cursor.execute("""
                    SELECT food_id FROM food WHERE fdc_id = %s;
                """, (fdc_id,))
                food_id = cursor.fetchone()[0]

                # Insert nutrient data only if foodNutrients is present and not empty
                if 'foodNutrients' in food and len(food['foodNutrients']) > 0:
                    for nutrient in food['foodNutrients']:
                        nutrient_name = nutrient['name']
                        nutrient_number = nutrient['number']
                        derivation_code = nutrient.get('derivationCode', None)
                        derivation_description = nutrient.get('derivationDescription', None)
                        amount = nutrient.get('amount', None)
                        unit_name = nutrient.get('unitName', None)

                        # Insert nutrient into nutrients table if it doesn't already exist
                        cursor.execute("""
                            INSERT INTO nutrients (nutrient_name, nutrient_number, derivation_code, derivation_description)
                            VALUES (%s, %s, %s, %s)
                            ON CONFLICT (nutrient_number) DO NOTHING;
                        """, (nutrient_name, nutrient_number, derivation_code, derivation_description))

                        # Get the nutrient_id from the nutrients table (whether newly inserted or existing)
                        cursor.execute("""
                            SELECT nutrient_id FROM nutrients WHERE nutrient_number = %s;
                        """, (nutrient_number,))
                        nutrient_id = cursor.fetchone()[0]

                        # Insert into food_nutrients table
                        cursor.execute("""
                            INSERT INTO food_nutrients (food_id, nutrient_id, amount, unit_name)
                            VALUES (%s, %s, %s, %s)
                            ON CONFLICT DO NOTHING;
                        """, (food_id, nutrient_id, amount, unit_name))
                else:
                    # Log if there are no food nutrients available for this food item
                    print(f"No nutrient data available for food with fdc_id {fdc_id}")
            else:
                # Log the non-dictionary food item
                print(f"Unexpected data format for food item: {food}")

        conn.commit()
        cursor.close()
        conn.close()

        # Rate limiting: wait 3.6 seconds between requests to adhere to the limit
        time.sleep(request_interval)

        page += 1

with DAG(
    dag_id='usda_food_data_import',
    default_args=default_args,
    description='DAG to import USDA food data using /foods/list',
    schedule_interval=None,
    start_date=datetime(2024, 10, 1),
    catchup=False
) as dag:

    import_data = PythonOperator(
        task_id='import_data',
        python_callable=fetch_and_store_food_data
    )

    import_data
