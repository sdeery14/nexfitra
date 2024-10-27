#!/bin/bash

# Load environment variables
set -e

# Run SQL commands
psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" <<-EOSQL
    CREATE TABLE food (
        fdc_id INT PRIMARY KEY,
        description TEXT,
        food_category TEXT,
        publication_date DATE
    );

    CREATE TABLE nutrients (
        nutrient_id INT PRIMARY KEY,
        nutrient_name TEXT,
        unit_name TEXT
    );

    CREATE TABLE food_nutrients (
        id SERIAL PRIMARY KEY,
        fdc_id INT REFERENCES food(fdc_id),
        nutrient_id INT REFERENCES nutrients(nutrient_id),
        amount FLOAT
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
EOSQL
