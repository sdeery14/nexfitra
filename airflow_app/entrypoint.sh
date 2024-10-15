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

# Execute the main command passed to the script
exec "$@"
