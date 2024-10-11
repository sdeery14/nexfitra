# NexFitra Development Plan

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Features](#2-features)
3. [Data Sources](#3-data-sources)
4. [Architecture](#4-architecture)
5. [Project Timeline](#5-project-timeline)
6. [Deployment Strategy](#6-deployment-strategy)
7. [CI/CD Pipeline](#7-cicd-pipeline)

## 1. Project Overview
NexFitra is a health app designed to help users create and track their workouts and diet. Users will input their information such as height, weight, sex, recent workout level, fitness goals, exercises they enjoy, and foods they like. The app will calculate the user's macros and use a generative AI model to suggest a workout schedule and meal plan. Users can save and track their progress, and the app will update the meal plan automatically when their height or weight changes.

## 2. Features
- **User Authentication:** Secure login and registration
- **User Profile Management:** Users can provide their fitness information and goals, and can update these over time. This will allow the model to create customized workout and meal plans. Users can also log workouts, meals, and track their fitness progress.
- **Workout Schedule and Meal Plan Suggestions:** Personalized workout schedules and meal plans generated based on user inputs. User can work with the generated plans or make their own, and the plans will adjust automatically when users update their profile. 
- **User Feedback:** Collect and integrate user feedback to continuously improve the app.

## 3. Data Sources
- **Nutrition Database**: Utilize a comprehensive nutrition database (e.g., USDA Food Data Central API) for accurate nutritional information of various foods.
- **Recipe Database**: Integrate with a recipe API (e.g., Spoonacular, Edamam) to access a wide variety of meal recipes.
- **Workout Exercise Database**: Create or integrate a database of various exercises, including descriptions, muscle groups targeted, and difficulty levels.
- **Data Storage**: Store frequently accessed data in the PostgreSQL database for quicker retrieval and to reduce API calls.
- **Data Update Schedule**: Implement a regular update schedule to keep the local database synchronized with the external data sources.

## 4. Architecture
- Frontend: 
  - React application for the user interface, interacting with the backend and AI API via RESTful APIs.
  - Bootstrap for responsive design and UI components.
- Backend:
  - Flask API: Handles business logic, user authentication, and communication with the database.
  - FastAPI Service: Handles generative AI tasks. A microservice for generating workout schedules and meal plans based on user data. Communicates with the Flask app.
- Database: PostgreSQL for storing user profiles, workout data, meal plans, and progress logs.
- AI Model: 
  - Generative AI model fine-tuned on fitness and nutrition datasets.
  - MLflow for experiment tracking, model versioning, and deployment.
- Data Layer:
  - PostgreSQL database will store user data, as well as cached nutrition information, recipes, and workout exercises.
  - API integrations with nutrition and recipe databases.
  - Custom workout exercise database integrated into the main PostgreSQL database.
- Data Access:
  - Flask backend will handle data retrieval and caching from external APIs.
  - FastAPI service will have direct access to the PostgreSQL database for AI model inference.
  - Implement a data access layer in both Flask and FastAPI services to manage database queries and external API calls.
- Security: Secure authentication with JWT tokens, data encryption for sensitive information, and role-based access control (RBAC).
- Scalability: Kubernetes for container orchestration, load balancing, and scaling. Separate services for the Flask app and FastAPI will allow independent scaling of the AI model when required.
- Monitoring and Logging: Tools such as Prometheus and Grafana for real-time performance monitoring and error logging.
- Backup and Recovery: Regular backups of user data and workout history to prevent data loss in case of failure.

## 5. Deployment Strategy
- Local Development: Use Docker Compose to spin up services locally. Both Flask and FastAPI will run in separate containers and interact over REST APIs.
- Staging Environment: Deploy the application to a Kubernetes cluster with separate services for Flask (backend), FastAPI (AI service), and PostgreSQL (database).
- Production Environment: Set up Kubernetes in a cloud environment (e.g., AWS, GCP) to handle scaling and orchestration for production traffic.
- Ensure proper configuration of API keys and database connections for accessing nutrition and recipe data in all environments.
- Set up scheduled tasks for regular updates of cached nutrition and recipe data.

## 6. CI/CD Pipeline
- Continuous Integration:
  - Automated tests for both Flask and FastAPI services.
  - Linting and static code analysis to ensure code quality.
- Continuous Deployment:
  - Automated deployment to Kubernetes using GitHub Actions.
  - Set up different environments (staging and production) with separate pipelines.
  - Docker image building for both Flask and FastAPI, pushed to a container registry (e.g., Docker Hub or AWS ECR).

  
## 7. Project Timeline
- **Week 1-2**: 
  - Set up the project development environment:
    - Docker containers for Flask, React, FastAPI, and PostgreSQL.
    - Docker Compose to set up services
  - Research and select nutrition and recipe APIs.
  - Design database schema to incorporate nutrition, recipe, and workout data.
- **Week 3-4**: 
  - Create the Flask and React components:
    - User authentication
    - User profile management
    - User intake form
    - Schedule page with manual schedule creation
    - Workouts page with manual workout creation
    - Diet page with manual diet creation
- **Week 5-6**: 
  - Create pipeline to generate workout plans and meal plans using MLFlow and FastAPI.
  - Test integration between Flask and FastAPI.
- **Week 7-8**: 
  - Add automatic workout and meal plan updates based on progress.
  - Optimize the AI model and integrate it with the frontend.
- **Week 9-10**: 
  - Finalize the CI/CD pipeline, and deploy to staging.
  - Perform end-to-end testing and bug fixes.
- **Week 11-12**: 
  - Launch the production environment and monitor for performance.
