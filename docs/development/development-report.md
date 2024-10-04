# NexFitra Development Report

## Table of Contents
1. [Project Overview](#1-project-overview)
2. [Technology Stack](#2-technology-stack)
3. [Features](#3-features)
4. [Architecture](#4-architecture)
5. [Development Setup](#5-development-setup)
6. [Development Steps](#6-development-steps)
7. [Deployment Strategy](#7-deployment-strategy)
8. [CI/CD Pipeline](#8-cicd-pipeline)
9. [Project Timeline](#9-project-timeline)
10. [Conclusion & Learnings](#10-conclusion--learnings)

## 1. Project Overview
This section provides a reflection on the original project overview and any changes or insights gained during development.

- **Original Overview**: NexFitra is a health app designed to help users create and track their workouts and diet. The app was planned to calculate macros and use a generative AI model to suggest workout schedules and meal plans.
- **Actual Implementation**: 
  - [To be filled as development progresses]
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
  - [To be updated as development progresses]
  - What changes were made? 
  - Were any new tools introduced? 
  - What were the pros and cons of the selected technologies?

## 3. Features
Track the development of each feature and the challenges encountered along the way.

- **User Authentication**: 
  - [To be filled as development progresses]
  - Was the implementation straightforward or were there issues with JWT tokens, role-based access, or third-party integrations?
- **User Profile Management**: 
  - [To be filled as development progresses]
  - Did you encounter any difficulties with handling user inputs, validation, or profile updates?
- **Workout and Meal Plan Suggestion**: 
  - [To be filled as development progresses]
  - What adjustments were made when integrating the AI model to generate plans?
  - Were there any performance issues or challenges in ensuring the accuracy of the AI-generated content?
- **Progress Tracking**: 
  - [To be filled as development progresses]
  - What were the difficulties in implementing data tracking?
  - Any challenges with data storage, visualization, or user feedback mechanisms?
  
## 4. Architecture
Discuss how the architecture evolved as you built the app.

- **Original Architecture**: Planned separation of concerns between frontend, backend, and AI services.
- **Actual Architecture**: 
  - [To be updated as development progresses]
  - Did the microservices architecture work as expected? 
  - Were there challenges with orchestrating the services?
  - Did you encounter any issues with integrating FastAPI and Flask?

## 5. Development Setup
This section provides a summary of the initial development setup for the NexFitra project.

### 5.1 Repository Initialization
- Created GitHub repository with README and LICENSE files

### 5.2 Application Structure
- Flask Backend: `flask_app/` with basic Flask application
- FastAPI Backend: `fastapi_app/` with basic FastAPI application
- React Frontend: `react_app/` created using Create React App

### 5.3 Dependency Management
- Installed Poetry for Python dependency management
- Created `pyproject.toml` files for Flask and FastAPI apps
- Locked dependencies using `poetry lock`

### 5.4 Docker Configuration
- Created Dockerfiles for:
  - Flask app and tests
  - FastAPI app and tests
  - React app

### 5.5 Environment Configuration
- Created `.env` file for sensitive data
- Provided `.env_template` for other developers

### 5.6 Service Orchestration
- Implemented `docker-compose.yaml` for local development
- Services: Flask, FastAPI, React, PostgreSQL databases, pgAdmin

### 5.7 Testing Setup
- Configured pytest for both Flask and FastAPI applications
- Created separate Docker services for running tests

### 5.8 Development Environment Usage
To run the development environment:
```bash
docker-compose up --build
```

To run tests:
```bash
docker-compose up --build flask_tests
docker-compose up --build fastapi_tests
```

## 6. Development Steps

### 6.1 Flask Backend
Provide a detailed report of the development and any obstacles encountered.

- **User Authentication**: 
  - [To be filled as development progresses]
  - How did the JWT implementation go?
  - Any difficulties with user session handling, expiration, or refreshing tokens?
  
- **User Profile**: 
  - [To be filled as development progresses]
  - How did you handle complex user data?
  - Were there any unexpected bugs or issues when integrating the user profile with the AI model?
  
- **Workout/Meal Plan Management**: 
  - [To be filled as development progresses]
  - How did you manage database interactions for storing plans? 
  - Were there challenges with ensuring data integrity or querying performance?

### 6.2 FastAPI AI Service
Provide insights into the development of the AI model and service.

- **AI Model Selection**: 
  - [To be filled as development progresses]
  - Which models did you initially choose? 
  - How did the testing and selection process go for different models? 
  - Were there any unexpected results in terms of accuracy or performance?
  
- **Model Training and Testing Pipeline**: 
  - [To be filled as development progresses]
  - How well did the model perform after training on the datasets? 
  - Were there any issues with the dataset preparation or handling large-scale fine-tuning?
  
- **Model Evaluation and Comparison**: 
  - [To be filled as development progresses]
  - Which model performed best in real-world tests? 
  - How did you handle performance testing (speed, accuracy, user feedback)?

- **AI Endpoints**: 
  - [To be filled as development progresses]
  - Were there any challenges with exposing the AI models via FastAPI endpoints? 
  - How did you manage the switching between different models during testing?

- **Optimization**: 
  - [To be filled as development progresses]
  - What optimization techniques worked best? 
  - Did ONNX or TensorRT lead to a notable improvement in inference times?

## 7. Deployment Strategy
Track your deployment progress and any issues.

- **Local Development**: 
  - [To be updated as development progresses]
  - Did the local development setup run smoothly with Docker Compose? 
  - Were there any challenges in syncing local development with Kubernetes configurations?
  
- **Staging & Production**: 
  - [To be updated as development progresses]
  - Did deployment to the Kubernetes cluster go as planned?
  - Were there any scaling issues or challenges in deploying the microservices?

## 8. CI/CD Pipeline
Reflect on your CI/CD setup and how it evolved.

- **GitHub Actions**: 
  - [To be updated as development progresses]
  - Was GitHub Actions sufficient for your CI/CD pipeline? 
  - Were there any integration issues with Docker and Kubernetes?
  
- **Automated Testing & Deployment**: 
  - [To be updated as development progresses]
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
    - 9/28: Set up Docker containers for Flask, FastAPI, PostgreSQL, and pgAdmin
    - 9/29: Set up test containers for Flask and FastAPI
    - 9/30: Set up container for React
    - 10/1: Set up separate database services for Flask, FastAPI, and test services.
    - 10/2: Created `setup.md` file
    - 10/3: Updated documentation
    - [To be updated as development progresses]

## 10. Conclusion & Learnings
Summarize your overall experience in developing NexFitra.

- [To be filled at the end of the project]
- What worked well?
- What would you change in the development process?
- Key takeaways for future projects.

## Next Steps
- Implement user authentication (Flask)
- Develop user profile functionality
- Create workout/meal plan management features
- Integrate AI model (FastAPI)
- Develop React frontend
- Implement comprehensive test suites
- Set up CI/CD pipeline