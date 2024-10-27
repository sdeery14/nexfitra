#!/bin/bash

# Load environment variables
set -e

# Run SQL commands
psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" <<-EOSQL
    CREATE TABLE food (
        food_id SERIAL PRIMARY KEY,
        fdc_id INT UNIQUE,
        description TEXT,
        data_type TEXT,
        publication_date DATE,
        brand_owner TEXT,
        gtin_upc TEXT,
        ndb_number INT,
        food_code TEXT
    );

    CREATE TABLE nutrients (
        nutrient_id SERIAL PRIMARY KEY,
        nutrient_name TEXT,
        nutrient_number TEXT UNIQUE,
        derivation_code TEXT,
        derivation_description TEXT
    );

    CREATE TABLE food_nutrients (
        food_nutrient_id SERIAL PRIMARY KEY,
        food_id INT REFERENCES food(food_id),
        nutrient_id INT REFERENCES nutrients(nutrient_id),
        amount FLOAT,
        unit_name TEXT,
        CONSTRAINT unique_food_nutrient UNIQUE (food_id, nutrient_id)
    );

    -- Create Airflow user
    DO
    \$\$
    BEGIN
        IF NOT EXISTS (SELECT FROM pg_roles WHERE rolname = '$USDA_DB_AIRFLOW_USER') THEN
            CREATE USER $USDA_DB_AIRFLOW_USER WITH PASSWORD '$USDA_DB_AIRFLOW_PASSWORD';
        END IF;
    END
    \$\$;

    -- Grant permissions
    GRANT CONNECT ON DATABASE $POSTGRES_DB TO $USDA_DB_AIRFLOW_USER;
    GRANT USAGE ON SCHEMA public TO $USDA_DB_AIRFLOW_USER;
    GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO $USDA_DB_AIRFLOW_USER;
    GRANT USAGE, SELECT ON SEQUENCE food_food_id_seq TO $USDA_DB_AIRFLOW_USER;
    GRANT USAGE, SELECT ON SEQUENCE nutrients_nutrient_id_seq TO $USDA_DB_AIRFLOW_USER;
    GRANT USAGE, SELECT ON SEQUENCE food_nutrients_food_nutrient_id_seq TO $USDA_DB_AIRFLOW_USER;
    
EOSQL
