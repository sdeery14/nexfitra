#!/bin/bash

set -e

echo "Checking if the Airflow database has already been initialized..."
if [ ! -f "/opt/airflow/initialized" ]; then
  echo "Initializing the Airflow database..."
  airflow db init
  if [ $? -eq 0 ]; then
    echo "Database initialized successfully."
    touch /opt/airflow/initialized
  else
    echo "Database initialization failed."
    exit 1
  fi
else
  echo "Database already initialized."
fi

echo "Checking if the Airflow admin user exists..."
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
