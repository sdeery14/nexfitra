#!/bin/bash
set -e

# Initialize the database if it doesn't exist
if [ ! -d "migrations" ]; then
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
else
    flask db upgrade
fi

exec "$@"
