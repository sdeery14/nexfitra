# NexFitra Development Report

## Table of Contents
1. [Project Overview](#1-project-overview)
2. [Technology Stack](#2-technology-stack)
3. [Features](#3-features)
4. [Architecture](#4-architecture)
5. [Development Setup](#5-development-setup)
   - [Set up GitHub Repo](#1-set-up-github-repo)
   - [Set up Bare Minimum Flask and FastAPI apps](#2-set-up-bare-minimum-flask-and-fastapi-apps)
   - [Set up Poetry](#3-set-up-poetry)
   - [Set up Docker](#4-set-up-docker)
6. [Detailed Development Steps](#6-detailed-development-steps)
   - [Flask Backend](#61-flask-backend)
   - [FastAPI AI Service](#62-fastapi-ai-service)
7. [Deployment Strategy](#7-deployment-strategy)
8. [CI/CD Pipeline](#8-cicd-pipeline)
9. [Project Timeline](#9-project-timeline)
10. [Conclusion & Learnings](#10-conclusion--learnings)

## 1. Project Overview
This section provides a reflection on the original project overview and any changes or insights gained during development.

- **Original Overview**: NexFitra is a health app designed to help users create and track their workouts and diet. The app was planned to calculate macros and use a generative AI model to suggest workout schedules and meal plans.
- **Actual Implementation**: 
  - Did the original scope stay the same? 
  - Were there any changes in the user flow or feature priorities?
  - What challenges arose with user inputs and automatic updates?

## 2. Technology Stack
Describe any deviations from the planned stack or tools, and discuss how they were resolved or improved.

- **Planned Stack**: 
  - Frontend: React 
  - Backend: Flask and FastAPI 
  - Database: PostgreSQL 
  - Orchestration: Kubernetes 
  - CI/CD: GitHub Actions
- **Actual Stack**:
  - What changes were made? 
  - Were any new tools introduced? 
  - What were the pros and cons of the selected technologies?

## 3. Features
Track the development of each feature and the challenges encountered along the way.

- **User Authentication**: 
  - Was the implementation straightforward or were there issues with JWT tokens, role-based access, or third-party integrations?
- **User Profile Management**: 
  - Did you encounter any difficulties with handling user inputs, validation, or profile updates?
- **Workout and Meal Plan Suggestion**: 
  - What adjustments were made when integrating the AI model to generate plans?
  - Were there any performance issues or challenges in ensuring the accuracy of the AI-generated content?
- **Progress Tracking**: 
  - What were the difficulties in implementing data tracking?
  - Any challenges with data storage, visualization, or user feedback mechanisms?
  
## 4. Architecture
Discuss how the architecture evolved as you built the app.

- **Original Architecture**: Planned separation of concerns between frontend, backend, and AI services.
- **Actual Architecture**: 
  - Did the microservices architecture work as expected? 
  - Were there challenges with orchestrating the services?
  - Did you encounter any issues with integrating FastAPI and Flask?

## 5. Development Setup

### 1. Set up GitHub Repo: 
  - Initialized the plan and report template as a git repo
  - Pushed the repo to a GitHub repo
  - Added README and LICENSE
### 2. Set up Bare Minimum Flask and FastAPI apps
- Created `flask_app` directory with an empty `__init__.py` file and an `app.py` file.
```python
# flask_app/app.py
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify(message="Hello from Flask!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

```
- Created `fastapi_app` directory with an empty `__init__.py` file and an `app.py` file.
```python
# fastapi_app/app.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

```
### 3. Set up Poetry:
  - Installed Poetry: `curl -sSL https://install.python-poetry.org | python3 -`
  - Created a Poetry file for the `flask_app`:
```toml
# flask_app/pyproject.toml
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
```bash
cd flask_app
poetry lock
```
  - Created a Poetry file for the `fastapi_app`:
```toml
# fastapi_app/pyproject.toml
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
```bash
cd ../fastapi_app
poetry lock
```
### 4. Set Up Docker: 
  - Created a .env file holding sensitive data, and made a .env_template for other developers.
```.env
# .env_template
# Use this template to change the defaults and set up your environemnt variables.
# Save the file as .env once the variables are changed
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_DB=nexfitra
PGADMIN_DEFAULT_EMAIL=admin@example.com
PGADMIN_DEFAULT_PASSWORD=admin

FLASK_DB_USER=flask_user
FLASK_DB_PASSWORD=flask_password
FLASK_DB_NAME=flask_db

FASTAPI_DB_USER=fastapi_user
FASTAPI_DB_PASSWORD=fastapi_password
FASTAPI_DB_NAME=fastapi_db
```
  - Created Dockerfiles for:
    - Flask (`flask_app/Dockerfile-flask`)
    - Flask Testing (`flask_app/Dockerfile-test`)
    - FastAPI (`fastapi_app/Dockerfile-fastapi`)
    - FastAPI Testing (`fastapi_app/Dockerfile-fastapi`)
```dockerfile
# flask_app/Dockerfile-flask

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
```dockerfile
# flask_app/Dockerfile-flask-test

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

```dockerfile
# fastapi_app/Dockerfile-fastapi

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
```dockerfile
# fastapi_app/Dockerfile-fastapi-test
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
  - Added script to create the database users and databases
```bash
# scripts/init-db.sh
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER $FLASK_DB_USER WITH PASSWORD '$FLASK_DB_PASSWORD';
    CREATE DATABASE $FLASK_DB_NAME;
    GRANT ALL PRIVILEGES ON DATABASE $FLASK_DB_NAME TO $FLASK_DB_USER;

    CREATE USER $FASTAPI_DB_USER WITH PASSWORD '$FASTAPI_DB_PASSWORD';
    CREATE DATABASE $FASTAPI_DB_NAME;
    GRANT ALL PRIVILEGES ON DATABASE $FASTAPI_DB_NAME TO $FASTAPI_DB_USER;
EOSQL
```
  - Used Docker Compose for local development to bring up both services (Flask and FastAPI) and the database.
```yaml
# docker-compose.yaml
version: '3.8'

services:
  flask:
    build:
      context: ./flask_app
      dockerfile: Dockerfile-flask
    container_name: flask_service
    ports:
      - "5000:5000"
    depends_on:
      - db
    environment:
      - DATABASE_URL=postgresql://${FLASK_DB_USER}:${FLASK_DB_PASSWORD}@db:5432/${FLASK_DB_NAME}
    networks:
      - nexfitra_network

  fastapi:
    build:
      context: ./fastapi_app
      dockerfile: Dockerfile-fastapi
    container_name: fastapi_service
    ports:
      - "8000:8000"
    depends_on:
      - db
    environment:
      - DATABASE_URL=postgresql://${FASTAPI_DB_USER}:${FASTAPI_DB_PASSWORD}@db:5432/${FASTAPI_DB_NAME}
    networks:
      - nexfitra_network

  db:
    image: postgres:16
    container_name: postgres_db
    environment:
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: ${POSTGRES_DB}
      FLASK_DB_USER: ${FLASK_DB_USER}
      FLASK_DB_PASSWORD: ${FLASK_DB_PASSWORD}
      FLASK_DB_NAME: ${FLASK_DB_NAME}
      FASTAPI_DB_USER: ${FASTAPI_DB_USER}
      FASTAPI_DB_PASSWORD: ${FASTAPI_DB_PASSWORD}
      FASTAPI_DB_NAME: ${FASTAPI_DB_NAME}
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./scripts/init-db.sh:/docker-entrypoint-initdb.d/init-db.sh
    networks:
      - nexfitra_network

  pgadmin:
    image: dpage/pgadmin4
    container_name: pgadmin_service
    environment:
      PGADMIN_DEFAULT_EMAIL: ${PGADMIN_DEFAULT_EMAIL}
      PGADMIN_DEFAULT_PASSWORD: ${PGADMIN_DEFAULT_PASSWORD}
    ports:
      - "5050:80"
    depends_on:
      - db
    volumes:
      - pgadmin_data:/var/lib/pgadmin
    networks:
      - nexfitra_network

volumes:
  postgres_data:
  pgadmin_data:

networks:
  nexfitra_network:

```
```bash
docker-compose up --build
```
- Results
  - The Flask app is available at http://127.0.0.1:5000/.
  - The Fast API is available at http://127.0.0.1:8000/.
  - The pgAdmin home page is available at http://127.0.0.1:5050/.
```bash
docker-compose up --build flask_tests
```
```bash
docker-compose up --build fastapi_tests
```
  
## 6. Detailed Development Steps

### 6.1 Flask Backend
Provide a detailed report of the development and any obstacles encountered.

- **User Authentication**: 
  - How did the JWT implementation go?
  - Any difficulties with user session handling, expiration, or refreshing tokens?
  
- **User Profile**: 
  - How did you handle complex user data?
  - Were there any unexpected bugs or issues when integrating the user profile with the AI model?
  
- **Workout/Meal Plan Management**: 
  - How did you manage database interactions for storing plans? 
  - Were there challenges with ensuring data integrity or querying performance?

### 6.2 FastAPI AI Service
Provide insights into the development of the AI model and service.

- **AI Model Selection**: 
  - Which models did you initially choose? 
  - How did the testing and selection process go for different models? 
  - Were there any unexpected results in terms of accuracy or performance?
  
- **Model Training and Testing Pipeline**: 
  - How well did the model perform after training on the datasets? 
  - Were there any issues with the dataset preparation or handling large-scale fine-tuning?
  
- **Model Evaluation and Comparison**: 
  - Which model performed best in real-world tests? 
  - How did you handle performance testing (speed, accuracy, user feedback)?

- **AI Endpoints**: 
  - Were there any challenges with exposing the AI models via FastAPI endpoints? 
  - How did you manage the switching between different models during testing?

- **Optimization**: 
  - What optimization techniques worked best? 
  - Did ONNX or TensorRT lead to a notable improvement in inference times?

## 7. Deployment Strategy
Track your deployment progress and any issues.

- **Local Development**: 
  - Did the local development setup run smoothly with Docker Compose? 
  - Were there any challenges in syncing local development with Kubernetes configurations?
  
- **Staging & Production**: 
  - Did deployment to the Kubernetes cluster go as planned?
  - Were there any scaling issues or challenges in deploying the microservices?

## 8. CI/CD Pipeline
Reflect on your CI/CD setup and how it evolved.

- **GitHub Actions**: 
  - Was GitHub Actions sufficient for your CI/CD pipeline? 
  - Were there any integration issues with Docker and Kubernetes?
  
- **Automated Testing & Deployment**: 
  - Did the automated tests and deployments run as expected?
  - Were there any bottlenecks or slowdowns in the pipeline?

## 9. Project Timeline
Compare the actual timeline to the planned one.

- **Planned Timeline**: 
  - Week 1-2: 9/28/2024-10/11/2024 Project Setup
  - Week 3-4: 10/12/2024-10/25/2024 User Authentication
  - Week 5-6: 10/26/2024-11/8/2024 Feature development
  - Week 7-8: 11/9/2024-11/22/2024 AI model integration
  - Week 9-10: 11/23/2024-12/6/2024 Set up CI/CD pipeline
  - Week 11-12: 12/7/2024-12/20/2024 Release app to production and monitor
  
- **Actual Timeline**:
  - Week 1-2: 9/28/2024-10/11/2024 Project Setup
    - 9/28/2024: set up docker containers for flask, fastapi, postgres, and pgadmin
    - 9/29/2024: set up test containers for flask and fastapi



## 10. Conclusion & Learnings
Summarize your overall experience in developing NexFitra.

- What worked well?
- What would you change in the development process?
- Key takeaways for future projects.
