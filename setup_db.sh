psql -U postgres -c "CREATE USER nexfitra_web_dev_user WITH PASSWORD '2P2yc7JuRvY5jx';"
psql -U postgres -c "CREATE DATABASE nexfitra_web_dev_db OWNER nexfitra_web_dev_user;"
psql -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE nexfitra_web_dev_db TO nexfitra_web_dev_user;"
