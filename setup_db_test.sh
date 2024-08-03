psql -U postgres -c "CREATE USER nexfitra_web_test_user WITH PASSWORD '5tn69b8QGRGb';"
psql -U postgres -c "CREATE DATABASE nexfitra_web_test_db OWNER nexfitra_web_test_user;"
psql -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE nexfitra_web_test_db TO nexfitra_web_test_user;"
