# NexFitra Development Plan

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Features](#2-features)
3. [Data Sources](#3-data-sources)
4. [Architecture](#4-architecture)
5. [Project Timeline](#5-project-timeline)


## 1. Project Overview
NexFitra is a health app designed to help users create and track their workouts and diet. Users will input their information such as height, weight, sex, recent workout level, fitness goals, exercises they enjoy, and foods they like. The app will calculate the user's macros and use a generative AI model to suggest a workout schedule and meal plan. Users can save and track their progress, and the app will update the meal plan automatically when their height or weight changes.

## 2. Features
- **User Authentication**: Secure login and registration
- **User Profile Management**: Users can provide their fitness information and goals, and can update these over time. This will allow the model to create customized workout and meal plans. Users can also log workouts, meals, and track their fitness progress.
- **Workout Schedule and Meal Plan Suggestions**: Personalized workout schedules and meal plans generated based on user inputs. User can work with the generated plans or make their own, and the plans will adjust automatically when users update their profile. 
- **User Feedback**: Collect and integrate user feedback to continuously improve the app.

## 3. Data Sources
- **Nutrition Database**: Utilize a comprehensive nutrition database (e.g., USDA Food Data Central API) for accurate nutritional information of various foods.
- **Recipe Database**: Integrate with a recipe API (e.g., Spoonacular, Edamam) to access a wide variety of meal recipes.
- **Workout Exercise Database**: Create or integrate a database of various exercises, including descriptions, muscle groups targeted, and difficulty levels.
- **Data Storage**: Store frequently accessed data in the PostgreSQL database for quicker retrieval and to reduce API calls.
- **Data Update Schedule**: Implement a regular update schedule to keep the local database synchronized with the external data sources.

## 4. Architecture
- **Development and Deployment Tools**:
  - Docker Compose for local development to spin up services locally.
  - Kubernetes for staging and production environments.
  - GitHub Actions for continuous integration and deployment.
  - Docker image building for both Flask and FastAPI, pushed to a container registry (e.g., Docker Hub or AWS ECR).
  - Automated tests, linting, and static code analysis to ensure code quality.
- **Frontend**: 
  - React application for the user interface, interacting with the backend and AI API via RESTful APIs.
  - Bootstrap for responsive design and UI components.
- **Backend**:
  - Flask API: Handles business logic, user authentication, and communication with the database.
  - FastAPI Service: Handles generative AI tasks. A microservice for generating workout schedules and meal plans based on user data. Communicates with the Flask app.
- **Database**: PostgreSQL for Flask (user profiles, workout data, meal plans, and progress logs) and FastAPI (MLFlow models and parameters).
  - Flask backend will handle data retrieval and caching from external APIs.
  - FastAPI service will have direct access to the Flask PostgreSQL database for AI model inference.
- **AI Model**: 
  - Generative AI model fine-tuned on fitness and nutrition datasets.
  - MLflow for experiment tracking, model versioning, and deployment.
- **Security**: Secure authentication with JWT tokens, data encryption for sensitive information, and role-based access control (RBAC).
- **Scalability**: Kubernetes for container orchestration, load balancing, and scaling. Separate services for the Flask app and FastAPI will allow independent scaling of the AI model when required.
- **Monitoring and Logging**: Tools such as Prometheus and Grafana for real-time performance monitoring and error logging.
- **Backup and Recovery**: Regular backups of user data and workout history to prevent data loss in case of failure.


## 5. Project Timeline
- **Week 1-2**: 
  - Set up the project development environment:
    - Docker containers for Flask, React, FastAPI, and PostgreSQL.
    - Docker Compose to set up services
  - Research and select nutrition and recipe APIs.
  - Design database schema to incorporate nutrition, recipe, and workout data.
- **Week 3-4**: 
  - Implement data ingestion pipeline using Apache Airflow:
    - Set up Airflow for orchestrating data ingestion tasks.
    - Create DAGs for ingesting data from nutrition and recipe APIs.
    - Ensure data is stored in PostgreSQL database.
- **Week 5-6**: 
  - Create the Flask and React components:
    - User authentication
    - User profile management
    - User intake form
    - Schedule page with manual schedule creation
    - Workouts page with manual workout creation
    - Diet page with manual diet creation
- **Week 7-8**: 
  - Create pipeline to generate workout plans and meal plans using MLFlow and FastAPI.
  - Test integration between Flask and FastAPI.
- **Week 9-10**: 
  - Add automatic workout and meal plan updates based on progress.
  - Optimize the AI model and integrate it with the frontend.
- **Week 11-12**: 
  - Finalize the CI/CD pipeline, and deploy to staging.
  - Perform end-to-end testing and bug fixes.
- **Week 13-14**: 
  - Launch the production environment and monitor for performance.
