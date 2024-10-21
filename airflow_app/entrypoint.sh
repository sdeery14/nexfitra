#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Initialize the Airflow database if it has not been done before
if [ ! -f "/opt/airflow/initialized" ]; then
  echo "Initializing the Airflow database..."
  airflow db migrate
  touch /opt/airflow/initialized
else
  echo "Database already initialized."
fi

# Check if the Airflow user exists, and create it if it doesn't
airflow users list | grep -q "${AIRFLOW_ADMIN_USERNAME}" || {
  echo "Creating Airflow admin user..."
  airflow users create \
    --username "${AIRFLOW_ADMIN_USERNAME}" \
    --firstname "${AIRFLOW_ADMIN_FIRSTNAME}" \
    --lastname "${AIRFLOW_ADMIN_LASTNAME}" \
    --role "${AIRFLOW_ADMIN_ROLE}" \
    --email "${AIRFLOW_ADMIN_EMAIL}" \
    --password "${AIRFLOW_ADMIN_PASSWORD}"
}

# Execute the main command passed to the script
exec "$@"
