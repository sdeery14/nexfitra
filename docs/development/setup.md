# Development Setup with Flask, FastAPI, React, Airflow, and PostgreSQL

## Table of Contents
1. [GitHub Repository Setup](#1-github-repository-setup)
2. [Set up Bare Minimum Applications](#2-set-up-bare-minimum-applications)
   1. [Flask Application](#21-flask-application)
   2. [FastAPI Application](#22-fastapi-application)
   3. [React Application](#23-react-application)
   4. [Airflow Application](#24-airflow-application)
3. [Environment Configuration](#3-environment-configuration)
4. [Set up Docker Compose for Service Orchestration](#4-set-up-docker-compose-for-service-orchestration)

## 1. GitHub Repository Setup

Create a directory for the project named `nexfitra` with the following directories and files. These files are filled out to record the development process and provide developers a guide to set up the project environment on their local machine.

- `nexfitra/`
  - `docs/`
    - `developer-guides/`
      - `setup.md`
    - `development/`
      - `development-plan.md`
      - `development-report.md`
      - `development-setup.md`
  - `.env`
  - `.env-template`
  - `.gitignore`
  - `LICENSE`
  - `README.md`

Use a `.gitignore` for python and make sure it contains `.env` to protect sensitive information.

```.gitignore
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#pdm.lock
#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
#   in version control.
#   https://pdm.fming.dev/latest/usage/project/#working-with-version-control
.pdm.toml
.pdm-python
.pdm-build/

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
#.idea/

```

Initialize the `nexfitra` directory` as a git repository.

Push the repository to GitHub.

## 2. Set up Bare Minimum Applications

Install Poetry using the official installation script:
```bash
curl -sSL https://install.python-poetry.org | python3 -
```
### 2.1 Flask Application

Create `flask_app` directory with the following structure.
- `flask_app/`
  - `tests/`
    - `test_app.py`
  - `__init__.py`
  - `app.py`
  - `Dockerfile-flas`
  - `Dockerfile-flask-test`
  - `pyproject.toml`


Leave the `__init__.py` file empty.

The `app.py` file contains a basic Flask application:
```python
# Import Flask and jsonify from the flask package
from flask import Flask, jsonify

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL ('/')
@app.route('/')
def hello():
    # Return a JSON response with a greeting message
    return jsonify(message="Hello from Flask!")

# Check if the script is run directly (and not imported as a module)
if __name__ == '__main__':
    # Run the Flask web server on host '0.0.0.0' and port '5000'
    app.run(host='0.0.0.0', port=5000)
```
The `test_app.py` file runs a simple test.
```python
import pytest
from app import app

# Define a pytest fixture named 'client' that sets up a test client for the Flask app
@pytest.fixture
def client():
    # Use the Flask app's test client for the duration of the test
    with app.test_client() as client:
        yield client  # Provide the test client to the test functions

# Define a test function that uses the 'client' fixture
def test_hello(client):
    # Send a GET request to the root URL of the Flask app
    response = client.get('/')
    
    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200
    
    # Assert that the response JSON data matches the expected dictionary
    assert response.get_json() == {"message": "Hello from Flask!"}
```

The `pyproject.toml` contains the dependencies for Flask application:
```toml
[tool.poetry]
name = "flask-app"
version = "0.1.0"
description = "Flask app for handling business logic and user authentication"
authors = ["Sean Deery <sean@nexfitra.com>"]

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
Lock the dependencies:
```bash
cd flask_app
poetry lock
cd ..
```
The `Dockerfile-flask` file sets up the environment to run the Flask app.
```dockerfile
# Use the official Python 3.12 image from the Docker Hub
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Poetry files and project dependencies to the working directory
COPY pyproject.toml poetry.lock ./

# Install Poetry and dependencies
RUN pip install poetry && poetry install --no-root

# Copy the rest of the Flask app code to the working directory
COPY . .

# Expose the port for Flask
EXPOSE 5000

# Command to run the Flask app
CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0", "--port=5000"]
```

The `Dockerfile-flask-test` sets up the environment to run the tests for the Flask app.
```dockerfile
# Use the official Python 3.12 image from the Docker Hub
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Poetry files and project dependencies to the working directory
COPY pyproject.toml poetry.lock ./

# Install Poetry and dependencies
RUN pip install poetry && poetry install --no-root

# Copy the rest of the Flask app code to the working directory
COPY . .

# Add /app to the Python path
ENV PYTHONPATH=/app

# Command to run the tests using Poetry
CMD ["poetry", "run", "pytest"]
```

Add the environment variables for the Flask app to the `.env` file.
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
Created `fastapi_app` directory with the following structure:
- `fastapi_app/`
  - `tests/`
    - `test_app.py`
  - `__init__.py`
  - `app.py`
  - `Dockerfile-fastapi`
  - `Dockerfile-fastapi-test`
  - `pyproject.toml`

Leave the `__init__.py` file empty.

The `app.py` file contains a basic FastAPI application:
```python
# Import FastAPI from the fastapi package
from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define a route for the root URL ('/')
@app.get("/")
def read_root():
    # Return a JSON response with a welcome message
    return {"message": "Hello from FastAPI!"}
```

The `pyproject.toml` contains the dependencies for FastAPI application:
```toml
[tool.poetry]
name = "fastapi-app"
version = "0.1.0"
description = "FastAPI app for serving AI-generated content"
authors = ["Sean Deery <sean@nexfitra.com>"]

[tool.poetry.dependencies]
python = "^3.12"
fastapi = "^0.95.2"
uvicorn = "^0.21.1"
transformers = "^4.28.0"
# Optional: torch or tensorflow depending on the models you're using
# torch = "^2.0.0"
# tensorflow = "^2.12.0"
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

Lock the dependencies.
```bash
cd fastapi_app
poetry lock
cd ..
```

The `Dockerfile-fastapi` sets up the environment to run the FastAPI app:
```dockerfile
# Use the official Python 3.12 image from the Docker Hub
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Poetry files and project dependencies to the working directory
COPY pyproject.toml poetry.lock ./

# Install Poetry and dependencies
RUN pip install poetry && poetry install --no-root

# Copy the rest of the FastAPI app code to the working directory
COPY . .

# Expose the port for FastAPI
EXPOSE 8000

# Command to run the FastAPI app
CMD ["poetry", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

The `Dockerfile-fastapi-test` sets up the environment to run the FastAPI tests:
```dockerfile
# Use the official Python 3.12 image from the Docker Hub
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Poetry files and project dependencies to the working directory
COPY pyproject.toml poetry.lock ./

# Install Poetry and dependencies
RUN pip install poetry && poetry install --no-root

# Copy the rest of the FastAPI app code to the working directory
COPY . .

# Add /app to the Python path
ENV PYTHONPATH=/app

# Command to run the tests using Poetry
CMD ["poetry", "run", "pytest", "-v"]
```

Add environment variables for `fastapi_app` to the `.env` file.
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
Create `react_app` directory using Create React App:
```bash
npx create-react-app react_app
```

Add `Dockerfile-react` to the `react_app` directory that sets up the environment to run the react app.
```dockerfile
FROM node:14-alpine

WORKDIR /app

# Install dependencies separately to leverage Docker caching
COPY package.json package-lock.json ./
RUN npm install

# Copy the rest of the app's source code
COPY . .

# Set the environment to development (can be overridden with Docker Compose)
ENV NODE_ENV=development

# Expose port 3000 (React development server's default port)
EXPOSE 3000

# Start the app in development mode
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

