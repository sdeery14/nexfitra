# Development Setup Report

## Table of Contents
1. [GitHub Repository Setup](#1-github-repository-setup)
2. [Application Setup](#2-application-setup)
3. [Dependency Management](#3-dependency-management)
4. [Docker Configuration](#4-docker-configuration)
5. [Environment Configuration](#5-environment-configuration)
6. [Service Orchestration](#6-service-orchestration)

## 1. GitHub Repository Setup
- Initialized the plan and report template as a git repository
- Pushed the repository to GitHub
- Added README and LICENSE files

## 2. Set up Bare Minimum Applications

Installed Poetry using the official installation script:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```
### 2.1 Flask Application
Created `flask_app` directory with:
- Empty `__init__.py` file
- `app.py` file containing a basic Flask application:
```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify(message="Hello from Flask!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

Created `pyproject.toml` for Flask application:
```toml
[tool.poetry]
name = "flask-app"
version = "0.1.0"
description = "Flask app for handling business logic and user authentication"
authors = ["Sean Deery sean@nexfitra.com"]

[tool.poetry.dependencies]
python = "^3.12"
flask = "^2.3.2"
flask-jwt-extended = "^4.4.4"
psycopg2-binary = "^2.9.7"
flask-sqlalchemy = "^3.0.4"

[tool.pytest.ini_options]
testpaths = ["tests"]

[tool.poetry.dev-dependencies]
pytest = "^8.3.3"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```
Locked dependencies:
```bash
cd flask_app
poetry lock
cd ..
```
Created `Dockerfile-flask` in the `flask_app` directory:
```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry install --no-root

COPY . .

EXPOSE 5000

CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0", "--port=5000"]
```

Created `Dockerfile-flask-test` in the `flask_app` directory:
```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry install --no-root

COPY . .

ENV PYTHONPATH=/app

CMD ["poetry", "run", "pytest"]
```

Created a `.env` file in the root directory and added the environment variables for flask.
```bash
# Flask application database configuration
FLASK_DB_USER=flask_user
FLASK_DB_PASSWORD=flask_password
FLASK_DB_NAME=flask_db
FLASK_DB_HOST=localhost
FLASK_DB_PORT=5432

# Flask test database configuration
FLASK_TEST_DB_USER=flask_test_user
FLASK_TEST_DB_PASSWORD=flask_test_password
FLASK_TEST_DB_NAME=flask_test_db
```

### 2.2 FastAPI Application
Created `fastapi_app` directory with:
- Empty `__init__.py` file
- `app.py` file containing a basic FastAPI application:
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}
```

Created `pyproject.toml` for FastAPI application:
```toml
[tool.poetry]
name = "fastapi-app"
version = "0.1.0"
description = "FastAPI app for serving AI-generated content"
authors = ["Sean Deery sean@nexfitra.com"]

[tool.poetry.dependencies]
python = "^3.12"
fastapi = "^0.95.2"
uvicorn = "^0.21.1"
transformers = "^4.28.0"
psycopg2-binary = "^2.9.7"

[tool.pytest.ini_options]
testpaths = ["tests"]

[tool.poetry.dev-dependencies]
pytest = "^8.3.3"
httpx = "^0.23.0"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

Locked dependencies:
```bash
cd fastapi_app
poetry lock
cd ..
```

Created `Dockerfile-fastapi` in the `fastapi_app` directory:
```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry install --no-root

COPY . .

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

Created `Dockerfile-fastapi-test` in the `fastapi_app` directory:
```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry install --no-root

COPY . .

ENV PYTHONPATH=/app

CMD ["poetry", "run", "pytest", "-v"]
```

Added environment variables for `fastapi_app` to the `.env` file.
```bash
# FastAPI application database configuration
FASTAPI_DB_USER=fastapi_user
FASTAPI_DB_PASSWORD=fastapi_password
FASTAPI_DB_NAME=fastapi_db

# FastAPI test database configuration
FASTAPI_TEST_DB_USER=fastapi_test_user
FASTAPI_TEST_DB_PASSWORD=fastapi_test_password
FASTAPI_TEST_DB_NAME=fastapi_test_db
```


### 2.3 React Application
Created `react_app` using Create React App:
```bash
npx create-react-app react_app
```

Created `Dockerfile-react` in the `react_app` directory:
```dockerfile
FROM node:14-alpine

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm install

COPY . .

ENV NODE_ENV=development

EXPOSE 3000

CMD ["npm", "start"]
```

### 2.4 Airflow Application
Created directory `airflow_app`.

Created the `pyproject.toml` in the `airflow_app` directory.

```toml
[tool.poetry]
name = "nexfitra-airflow"
version = "0.1.0"
description = "Airflow setup for pulling data from USDA API to Flask database"
authors = ["Sean Deery <sean@nexfitra.com>"]
license = "MIT"

[tool.poetry.dependencies]
python = "^3.12"
apache-airflow = "^2.5.1"
psycopg2-binary = "^2.9.3" # PostgreSQL adapter for Airflow DB and Flask DB connection
requests = "^2.31.0" # For making HTTP requests to USDA API
cryptography = "^3.4.8" # Used for generating Fernet keys and required by Airflow
sqlalchemy = "^1.4" # ORM for database operations

[tool.poetry.extras]
# Optional extras if needed, e.g., depending on specific use cases
# aws = ["apache-airflow[amazon]"]
# gcp = ["apache-airflow[gcp]"]

[tool.poetry.dev-dependencies]
pytest = "^7.4.0" # Unit testing
pytest-cov = "^4.1.0" # Code coverage reporting for tests

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

Created `Dockerfile-airflow` in the `airflow_app` directory.

```Dockerfile
# Use the official Apache Airflow image from Docker Hub
FROM apache/airflow:2.10.2

# Set the working directory inside the container
WORKDIR /opt/airflow

# Copy the Poetry files and project dependencies to the working directory
COPY pyproject.toml poetry.lock ./

# Install Poetry and dependencies
RUN pip install poetry && poetry install --no-root

# Copy the rest of the Airflow DAGs and files to the working directory
COPY . .

# Expose the port for the Airflow webserver
EXPOSE 8080

# Command to run the Airflow scheduler (you can adjust this for webserver, etc.)
CMD ["poetry", "run", "airflow", "scheduler"]
```

Created Fernet key
```bash
python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
```

Created secret key for Airflow.
```
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

Added environment variables to `.env` file.
```bash
# Airflow database configuration
AIRFLOW_DB_USER=airflow_user
AIRFLOW_DB_PASSWORD=airflow_password
AIRFLOW_DB_NAME=airflow_db
AIRFLOW_DB_HOST=airflow_db
AIRFLOW_DB_PORT=5432

# Airflow configuration
AIRFLOW_FERNET_KEY=airflow_fernet_key
AIRFLOW_SECRET_KEY=airflow_secret_key
```


## 3. Environment Configuration
Below is the full environment variables template `env_template`:
```bash
# .env_template
# Save the file as .env and use as a template to change the defaults and set up your environemnt variables.

# Flask application database configuration
FLASK_DB_USER=flask_user
FLASK_DB_PASSWORD=flask_password
FLASK_DB_NAME=flask_db

# Flask test database configuration
FLASK_TEST_DB_USER=flask_test_user
FLASK_TEST_DB_PASSWORD=flask_test_password
FLASK_TEST_DB_NAME=flask_test_db

# FastAPI application database configuration
FASTAPI_DB_USER=fastapi_user
FASTAPI_DB_PASSWORD=fastapi_password
FASTAPI_DB_NAME=fastapi_db

# FastAPI test database configuration
FASTAPI_TEST_DB_USER=fastapi_test_user
FASTAPI_TEST_DB_PASSWORD=fastapi_test_password
FASTAPI_TEST_DB_NAME=fastapi_test_db

# pgAdmin configuration
PGADMIN_DEFAULT_EMAIL=admin@example.com
PGADMIN_DEFAULT_PASSWORD=admin
```

## 4. Set up Docker Compose for Service Orchestration

Added environment variables for pgAdmin to the `.env` file.
```
# pgAdmin configuration
PGADMIN_DEFAULT_EMAIL=admin@example.com
PGADMIN_DEFAULT_PASSWORD=admin
```

Created `docker-compose.yaml` for local development:
```yaml
services:
  flask_service:
    build:
      context: ./flask_app
      dockerfile: Dockerfile-flask
    ports:
      - "5000:5000"
    depends_on:
      - flask_db_service
    environment:
      - DATABASE_URL=postgresql://${FLASK_DB_USER}:${FLASK_DB_PASSWORD}@db:5432/${FLASK_DB_NAME}
    networks:
      - nexfitra_network

  flask_test_service:
    build:
      context: ./flask_app
      dockerfile: Dockerfile-flask-test
    depends_on:
      - flask_test_db_service
    environment:
      - DATABASE_URL=postgresql://${FLASK_TEST_DB_USER}:${FLASK_TEST_DB_PASSWORD}@db:5432/${FLASK_TEST_DB_NAME}
    networks:
      - nexfitra_network

  react-service:
    build:
      context: ./react_app 
      dockerfile: Dockerfile-react
    ports:
      - "3000:3000"
    volumes:
      - ./react_app:/app/react_app
      - react_app_node_modules:/app/react_app/node_modules
    depends_on:
      - flask_service
    networks:
      - nexfitra_network

  fastapi_service:
    build:
      context: ./fastapi_app
      dockerfile: Dockerfile-fastapi
    ports:
      - "8000:8000"
    depends_on:
      - fastapi_db_service
    environment:
      - DATABASE_URL=postgresql://${FASTAPI_DB_USER}:${FASTAPI_DB_PASSWORD}@db:5432/${FASTAPI_DB_NAME}
    networks:
      - nexfitra_network

  fastapi_test_service:
    build:
      context: ./fastapi_app
      dockerfile: Dockerfile-fastapi-test
    depends_on:
      - fastapi_test_db_service
    environment:
      - DATABASE_URL=postgresql://${FASTAPI_DB_USER}:${FASTAPI_DB_PASSWORD}@db:5432/${FASTAPI_DB_NAME}
    command: ["poetry", "run", "pytest", "-v"]
    networks:
      - nexfitra_network

  flask_db_service:
    image: postgres:16
    environment:
      POSTGRES_USER: ${FLASK_DB_USER}
      POSTGRES_PASSWORD: ${FLASK_DB_PASSWORD}
      POSTGRES_DB: ${FLASK_DB_NAME} 
    ports:
      - "5432:5432"
    volumes:
      - flask_postgres_data:/var/lib/postgresql/data
    networks:
      - nexfitra_network
  
  flask_test_db_service:
    image: postgres:16
    environment:
      POSTGRES_USER: ${FLASK_TEST_DB_USER}
      POSTGRES_PASSWORD: ${FLASK_TEST_DB_PASSWORD}
      POSTGRES_DB: ${FLASK_TEST_DB_NAME}
    ports:
      - "5433:5432"
    volumes:
      - flask_test_postgres_data:/var/lib/postgresql/data
    networks:
      - nexfitra_network

  fastapi_db_service:
    image: postgres:16
    environment:
      POSTGRES_USER: ${FASTAPI_DB_USER}
      POSTGRES_PASSWORD: ${FASTAPI_DB_PASSWORD}
      POSTGRES_DB: ${FASTAPI_DB_NAME}
    ports:
      - "5434:5432"
    volumes:
      - fastapi_postgres_data:/var/lib/postgresql/data
    networks:
      - nexfitra_network
  
  fastapi_test_db_service:
    image: postgres:16
    environment:
      POSTGRES_USER: ${FASTAPI_TEST_DB_USER}
      POSTGRES_PASSWORD: ${FASTAPI_TEST_DB_PASSWORD}
      POSTGRES_DB: ${FASTAPI_TEST_DB_NAME}
    ports:
      - "5435:5432"
    volumes:
      - fastapi_test_postgres_data:/var/lib/postgresql/data
    networks:
      - nexfitra_network

  pgadmin_service:
    image: dpage/pgadmin4
    environment:
      PGADMIN_DEFAULT_EMAIL: ${PGADMIN_DEFAULT_EMAIL}
      PGADMIN_DEFAULT_PASSWORD: ${PGADMIN_DEFAULT_PASSWORD}
    ports:
      - "5050:80"
    depends_on:
      - flask_db_service
      - flask_test_db_service
      - fastapi_db_service
      - fastapi_test_db_service  
    volumes:
      - pgadmin_data:/var/lib/pgadmin
    networks:
      - nexfitra_network

volumes:
  flask_postgres_data:
  flask_test_postgres_data:
  fastapi_postgres_data:
  fastapi_test_postgres_data:
  pgadmin_data:
  react_app_node_modules:

networks:
  nexfitra_network:
```

