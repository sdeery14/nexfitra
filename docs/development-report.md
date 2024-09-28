# NexFitra Development Report

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

1. **Set up GitHub Repo**: 

This section will reflect on the ease or difficulty of setting up the environment.

- **Poetry**: 
  - Was Poetry sufficient for dependency management? 
  - Were there any challenges getting it to work with Docker and Kubernetes?
- **Docker & Kubernetes**: 
  - What challenges did you encounter with setting up Dockerfiles or Docker Compose? 
  - Did the Kubernetes setup scale as expected for development?
  
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
  - Week 1-2: Project setup
  - Week 3-4: User Authentication
  - Week 5-6: Feature development
  - Week 7-8: AI model integration, etc.
  
- **Actual Timeline**:
  - Did you stick to the original timeline?
  - Where were the major delays, and what caused them?

## 10. Conclusion & Learnings
Summarize your overall experience in developing NexFitra.

- What worked well?
- What would you change in the development process?
- Key takeaways for future projects.
