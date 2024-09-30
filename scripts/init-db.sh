#!/bin/bash
# Exit immediately if a command exits with a non-zero status
set -e

# Connect to PostgreSQL using the provided username and database name
# and execute the following SQL commands
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    -- Create a user for the Flask application with the specified password
    CREATE USER $FLASK_DB_USER WITH PASSWORD '$FLASK_DB_PASSWORD';
    
    -- Create a database for the Flask application
    CREATE DATABASE $FLASK_DB_NAME;
    
    -- Grant all privileges on the Flask database to the Flask user
    GRANT ALL PRIVILEGES ON DATABASE $FLASK_DB_NAME TO $FLASK_DB_USER;

    -- Create a user for the FastAPI application with the specified password
    CREATE USER $FASTAPI_DB_USER WITH PASSWORD '$FASTAPI_DB_PASSWORD';
    
    -- Create a database for the FastAPI application
    CREATE DATABASE $FASTAPI_DB_NAME;
    
    -- Grant all privileges on the FastAPI database to the FastAPI user
    GRANT ALL PRIVILEGES ON DATABASE $FASTAPI_DB_NAME TO $FASTAPI_DB_USER;
EOSQL