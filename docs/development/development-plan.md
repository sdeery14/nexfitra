# NexFitra Development Plan

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Technology Stack](#2-technology-stack)
   1. [Technology Stack Summary](#21-technology-stack-summary)
   2. [Technology Stack Details](#22-technology-stack-details)
3. [Features](#3-features)
4. [Architecture](#4-architecture)
5. [Development Setup](#5-development-setup)
6. [Detailed Development Steps](#6-detailed-development-steps)
   1. [Flask Backend](#61-flask-backend)
   2. [FastAPI AI Service](#62-fastapi-ai-service)
7. [Deployment Strategy](#7-deployment-strategy)
8. [CI/CD Pipeline](#8-cicd-pipeline)
9. [Project Timeline](#9-project-timeline)


## 1. Project Overview
NexFitra is a health app designed to help users create and track their workouts and diet. Users will input their information such as height, weight, sex, recent workout level, fitness goals, exercises they enjoy, and foods they like. The app will calculate the user's macros and use a generative AI model to suggest a workout schedule and meal plan. Users can save and track their progress, and the app will update the meal plan automatically when their height or weight changes.

## 2. Technology Stack

### 2.1 Technology Stack Summary
- **Frontend**: React
- **Backend**: Flask (Business Logic & User Authentication), FastAPI (Generative AI Service)
- **Database**: PostgreSQL
- **Database Management**: pgAdmin
- **Containerization**: Docker
- **Orchestration**: Kubernetes
- **CI/CD**: GitHub Actions (CI/CD Pipeline for automatic deployments)
- **Dependency Management**: Poetry

### 2.2 Technology Stack Details
- **Frontend**: **React**
  - **Justification**: React is a highly popular JavaScript library for building user interfaces, particularly single-page applications (SPAs). It offers a component-based architecture, which enhances reusability and simplifies UI development. React’s ecosystem includes rich state management tools like Redux, and integration with other libraries is seamless. Given its large community support and continuous updates, React is well-suited for building responsive, dynamic, and scalable web applications.
  - **Benefits**: 
    - Strong community and ecosystem
    - Reusable components
    - Easy integration with backend APIs
    - High performance through virtual DOM

- **Backend**: **Flask (Business Logic & User Authentication)** and **FastAPI (Generative AI Service)**
  - **Flask**:
    - **Justification**: Flask is a microframework for Python that is simple yet powerful. It’s lightweight, making it easy to build and scale small applications while retaining the flexibility to add extensions for more advanced use cases (e.g., authentication with Flask-JWT-Extended, database interactions with SQLAlchemy). Flask's minimalism ensures that only necessary components are included, resulting in faster development cycles. It’s ideal for handling the business logic, user authentication, and routing in the NexFitra app.
    - **Benefits**: 
      - Lightweight and flexible
      - Active community support
      - Easily extensible with Flask plugins
      - Familiar to many developers due to Python’s popularity

  - **FastAPI**:
    - **Justification**: FastAPI is a modern, high-performance web framework for building APIs with Python, particularly optimized for asynchronous operations. It is known for its simplicity, automatic validation, and speed, making it perfect for AI services that may require intensive computations. FastAPI allows the development of APIs that are easily scalable and can handle high-throughput scenarios, which is important for serving AI-generated content in NexFitra.
    - **Benefits**: 
      - High performance and asynchronous support
      - Built-in validation and serialization using Python type hints
      - Auto-generated OpenAPI documentation
      - Easy to integrate with AI models and services

- **Database**: **PostgreSQL**
  - **Justification**: PostgreSQL is an open-source, relational database management system known for its stability, extensibility, and support for complex queries. It is well-suited for applications requiring ACID compliance and complex transactions, such as fitness tracking apps where user data must be stored and retrieved efficiently. PostgreSQL also supports JSON data types and full-text search, making it a versatile choice for modern web applications.
  - **Benefits**:
    - ACID-compliant transactions for reliability
    - Rich feature set including JSON support and advanced indexing
    - Open-source with an active development community
    - Scalable and suitable for handling large datasets

- **Database Management**: **pgAdmin**
  - **Justification**: pgAdmin is the most popular and feature-rich open-source administration tool for PostgreSQL. It provides an intuitive web interface for managing PostgreSQL databases, making it easier to handle day-to-day tasks such as running queries, managing tables, and performing backups. This makes pgAdmin an ideal choice for managing NexFitra’s user profiles, workout data, and meal plans.
  - **Benefits**:
    - User-friendly web interface
    - Rich feature set for database management
    - Supports backups, monitoring, and fine-grained administrative tasks

- **Containerization**: **Docker**
  - **Justification**: Docker allows for containerization, enabling developers to package applications and their dependencies into a single container that can run consistently across various environments. This is essential for NexFitra, where maintaining uniform development, testing, and production environments is critical for reliability. Docker’s lightweight containers also make it easier to deploy microservices, such as Flask and FastAPI, as independent units.
  - **Benefits**:
    - Consistent development and production environments
    - Simplifies dependency management
    - Lightweight and efficient containerization
    - Easy to scale and orchestrate microservices

- **Orchestration**: **Kubernetes**
  - **Justification**: Kubernetes is a leading container orchestration tool used to automate the deployment, scaling, and management of containerized applications. For NexFitra, Kubernetes ensures that both the Flask backend and FastAPI AI service can scale automatically based on demand, providing high availability and resilience. It allows NexFitra to easily manage container lifecycles, implement load balancing, and achieve zero downtime deployments.
  - **Benefits**:
    - Automates scaling, deployment, and management of containers
    - Load balancing and self-healing of containers
    - Supports rolling updates for zero downtime
    - Widely adopted with strong community and tool support

- **CI/CD**: **GitHub Actions**
  - **Justification**: GitHub Actions provides a flexible and powerful way to automate the CI/CD process directly from GitHub repositories. With NexFitra, GitHub Actions can automate the build, test, and deployment processes for both the Flask and FastAPI services, reducing manual work and the risk of errors. It integrates smoothly with Docker and Kubernetes, allowing for continuous deployment to staging and production environments.
  - **Benefits**:
    - Seamless integration with GitHub repositories
    - Custom workflows for building, testing, and deploying
    - Supports multi-environment deployments (e.g., staging and production)
    - Extensive marketplace of pre-built actions and integrations

- **Dependency Management**: **Poetry**
  - **Justification**: Poetry is a dependency management and packaging tool for Python that simplifies project setup, dependency resolution, and virtual environment management. It is particularly useful for managing multiple Python projects (Flask and FastAPI) within the same codebase. Poetry ensures that dependencies are locked and reproducible across different environments, which is essential for ensuring consistency in development, testing, and production.
  - **Benefits**:
    - Easy to manage dependencies and virtual environments
    - Lockfile ensures consistency across environments
    - Simplifies Python project setup and packaging
    - Supports publishing packages to PyPI if needed

## 3. Features
- **User Authentication**: Secure login and registration
- **User Profile Management**: Users can update their information such as height, weight, sex, and fitness goals.
- **Workout Schedule Suggestion**: Personalized workout schedules generated based on user inputs.
- **Meal Plan Suggestion**: AI-generated meal plans based on macronutrient and caloric needs.
- **Progress Tracking**: Users can log workouts, meals, and track their fitness progress.
- **Automatic Meal Plan Update**: Meal plans will adjust when users update their profile (e.g., weight changes).
- **Integration with Generative AI Model**: AI model deployed via FastAPI to suggest workout schedules and meal plans.
- **Security Considerations**: Data encryption, secure authentication, and authorization mechanisms.
- **Scalability**: Load balancing, container orchestration (Kubernetes), and database scaling.
- **Monitoring and Logging**: Application performance monitoring and error tracking.
- **Backup and Recovery**: Data backup and recovery strategies.
- **User Feedback**: Collect and integrate user feedback to continuously improve the app.

## 4. Architecture
- **Frontend**: A React application for the user interface, interacting with the backend and AI API via RESTful APIs.
- **Backend**:
  - **Flask API**: Handles business logic, user authentication, and communication with the database.
  - **FastAPI Service**: Handles generative AI tasks. A microservice for generating workout schedules and meal plans based on user data.
- **Database**: PostgreSQL is used for storing user profiles, workout data, meal plans, and progress logs.
- **AI Model**: The generative AI model is fine-tuned on fitness and nutrition datasets and deployed via FastAPI. It uses input such as user profile data (e.g., height, weight, goals) to generate personalized workout and meal plans.
- **Security**: Secure authentication with JWT tokens, data encryption for sensitive information, and role-based access control (RBAC).
- **Scalability**: Kubernetes will handle container orchestration, load balancing, and scaling. Separate services for the Flask app and FastAPI will allow independent scaling of the AI model when required.
- **Monitoring and Logging**: Tools such as Prometheus and Grafana for real-time performance monitoring and error logging.
- **Backup and Recovery**: Regular backups of user data and workout history to prevent data loss in case of failure.

## 5. Development Setup
1. **Clone the Repository**: `git clone https://github.com/yourusername/nexfitra.git`
2. **Navigate to the Project Directory**: `cd nexfitra`
3. **Set Up Poetry**:
   - Install Poetry: `curl -sSL https://install.python-poetry.org | python3 -`
   - Initialize Poetry in the project: `poetry init`
   - Add dependencies (e.g., Flask, FastAPI, PostgreSQL, etc.) via Poetry: `poetry add flask fastapi uvicorn psycopg2-binary`
4. **Set Up Docker**: 
   - Create Dockerfiles for both Flask (`Dockerfile-flask`) and FastAPI (`Dockerfile-fastapi`).
   - Use Docker Compose for local development to bring up both services (Flask and FastAPI) and the database.
5. **Run Docker Compose**: `docker-compose up --build`
   - Access the **Flask App** at `http://localhost:5000`
   - Access the **FastAPI Service** at `http://localhost:8000`
6. **Access the Application**: Open `http://localhost:3000` for the frontend and interact with the backend Flask API and AI FastAPI service through their respective endpoints.

## 6. Detailed Development Steps

### 6.1 Flask Backend
- **User Authentication**: Implement secure login and registration using Flask with JWT authentication.
- **User Profile**: Build REST endpoints to manage user profiles (height, weight, sex, fitness goals, etc.).
- **Workout/Meal Plan Management**: Store and retrieve workout and meal plans from the PostgreSQL database.
- **Progress Tracking**: Build endpoints to log user progress (weight changes, workout completion, etc.).

### 6.2 FastAPI AI Service
- **AI Model Selection**:
  - Choose several base models from **Hugging Face**, **LLaMA**, or other sources. Start with generative text models that perform well in fitness and nutrition contexts.
  - Models to evaluate could include GPT-2, GPT-3, LLaMA, BART, and T5.
  - Fine-tune the selected models on fitness and nutrition datasets.
  
- **Model Training and Testing Pipeline**:
  - Set up a pipeline to experiment with different models. Create a training script that supports easy switching between different models and datasets.
  - Use `transformers.Trainer` from Hugging Face to fine-tune models:
    ```python
    from transformers import AutoModelForCausalLM, Trainer, TrainingArguments
    
    def fine_tune_model(model_name, dataset):
        model = AutoModelForCausalLM.from_pretrained(model_name)
        trainer = Trainer(
            model=model,
            args=TrainingArguments(output_dir="./results", num_train_epochs=3),
            train_dataset=dataset
        )
        trainer.train()
    ```

- **Model Evaluation and Comparison**:
  - Implement evaluation scripts that compare the models based on metrics like inference time, response quality, and user satisfaction. Use these metrics to determine the best model.
  - Test different models on real-world examples by integrating them into the FastAPI service, then log the results (e.g., speed, accuracy, user feedback).
  - Automate the evaluation process using A/B testing on a subset of users.
  
- **AI Endpoints**:
  - `POST /generate-plan`: Takes user profile data as input and returns a personalized workout schedule and meal plan.
  - Incorporate a mechanism to switch between models for evaluation. For example, pass a parameter in the request to choose the model, or automate the selection for A/B testing.
  
- **Optimization**:
  - Optimize the best-performing model using ONNX or TensorRT for faster inference in production.
  - Deploy the optimized model via FastAPI as a scalable microservice using Kubernetes.

- **Deployment**:
  - Package the FastAPI service and AI model in a Docker container.
  - Ensure that the FastAPI service scales independently in the Kubernetes cluster based on usage and load.

## 7. Deployment Strategy
- **Local Development**: Use Docker Compose to spin up services locally. Both Flask and FastAPI will run in separate containers and interact over REST APIs.
- **Staging Environment**: Deploy the application to a Kubernetes cluster with separate services for Flask (backend), FastAPI (AI service), and PostgreSQL (database).
- **Production Environment**: Set up Kubernetes in a cloud environment (e.g., AWS, GCP) to handle scaling and orchestration for production traffic.

## 8. CI/CD Pipeline
- **Continuous Integration**:
  - Automated tests for both Flask and FastAPI services.
  - Linting and static code analysis to ensure code quality.
- **Continuous Deployment**:
  - Automated deployment to Kubernetes using GitHub Actions.
  - Set up different environments (staging and production) with separate pipelines.
  - Docker image building for both Flask and FastAPI, pushed to a container registry (e.g., Docker Hub or AWS ECR).

## 9. Project Timeline
- **Week 1-2**: 
  - Set up the project structure, Docker containers for Flask, FastAPI, and PostgreSQL.
  - Basic UI setup in React.
- **Week 3-4**: 
  - Implement user authentication and profile management in Flask.
  - Develop and deploy the FastAPI service for the AI model.
- **Week 5-6**: 
  - Build endpoints for workout schedule and meal plan suggestions.
  - Test integration between Flask and FastAPI.
- **Week 7-8**: 
  - Add progress tracking and automatic meal plan updates.
  - Optimize the AI model and integrate it with the frontend.
- **Week 9-10**: 
  - Write tests, finalize the CI/CD pipeline, and deploy to staging.
  - Perform end-to-end testing and bug fixes.
- **Week 11-12**: 
  - Launch the production environment and monitor for performance.
