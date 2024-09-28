# NexFitra Development Plan

## 1. Project Overview
NexFitra is a health app designed to help users create and track their workouts and diet. Users will input their information such as height, weight, sex, recent workout level, fitness goals, exercises they enjoy, and foods they like. The app will calculate the user's macros and use a generative AI model to suggest a workout schedule and meal plan. Users can save and track their progress, and the app will update the meal plan automatically when their height or weight changes.

## 2. Technology Stack
- **Frontend**: React
- **Backend**: Flask (Business Logic & User Authentication), FastAPI (Generative AI Service)
- **Database**: PostgreSQL
- **Database Management**: pgAdmin
- **Containerization**: Docker
- **Orchestration**: Kubernetes
- **CI/CD**: GitHub Actions (CI/CD Pipeline for automatic deployments)
- **Dependency Management**: Poetry

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
