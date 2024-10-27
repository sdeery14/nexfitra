from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import requests
import psycopg2

default_args = {
    'owner': 'airflow',
    'retries': 5,
    'retry_delay': timedelta(minutes=5),
}

def fetch_and_store_food_data(**kwargs):
    USDA_API_KEY = "your_usda_api_key"
    page = 1
    page_size = 100  # Adjust based on your needs

    while True:
        url = f"https://api.nal.usda.gov/fdc/v1/foods/list?api_key={USDA_API_KEY}&pageSize={page_size}&pageNumber={page}"
        response = requests.get(url)
        data = response.json()

        if not data:
            break  # Stop if no more data

        # Connect to your Postgres database
        conn = psycopg2.connect(
            dbname="your_db_name",
            user="your_db_user",
            password="your_db_password",
            host="your_db_host"
        )
        cursor = conn.cursor()

        for food in data:
            cursor.execute("""
                INSERT INTO food (fdc_id, description, food_category, publication_date)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (fdc_id) DO NOTHING;
            """, (food['fdcId'], food['description'], food['foodCategory'], food['publicationDate']))

        conn.commit()
        cursor.close()
        conn.close()

        page += 1

with DAG(
    dag_id='usda_food_data_import',
    default_args=default_args,
    description='DAG to import USDA food data using /foods/list',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 10, 1),
    catchup=False
) as dag:

    import_data = PythonOperator(
        task_id='import_data',
        python_callable=fetch_and_store_food_data
    )

    import_data
