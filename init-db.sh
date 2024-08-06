#!/bin/bash
set -e

# Read the secrets from the files
FLASK_USER_PASSWORD=$(cat /run/secrets/flask_user_password)
FLASK_TEST_USER_PASSWORD=$(cat /run/secrets/flask_test_user_password)

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER flask_user WITH PASSWORD '$FLASK_USER_PASSWORD';
    CREATE DATABASE flask_db OWNER flask_user;

    CREATE USER flask_test_user WITH PASSWORD '$FLASK_TEST_USER_PASSWORD';
    CREATE DATABASE flask_test_db OWNER flask_test_user;

EOSQL
