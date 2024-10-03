# Development Setup Instructions

### 1. **Clone the repository:**
First, clone the NexFitra repository and navigate to the project directory:
```bash
git clone https://github.com/yourusername/nexfitra.git
cd nexfitra
```
### 2. **Set Up Environment Variables**
Next, create the `.env` file from the provided `.env_template` file:
```bash
# Copy the template to a .env file
cp .env_template .env
```

### 3. **Update Environment Variables**
Open the .env file and update the environment variables to secure values. Ensure that passwords and sensitive data are strong and unique:
```bash
nano .env
```
Edit and replace the placeholders with your secure credentials (e.g., database users, passwords, etc.).

### 4. **Build the Docker Images and Start the Services**
Once the environment variables are configured, build the Docker images and start the services:
```bash
docker-compose up --build
```
This command will pull the necessary Docker images, build the containers, and start all the services (Flask, FastAPI, React, PostgreSQL, pgAdmin, etc.).

The test services can also be run independently for each app:
```bash
docker-compose up --build flask_tests
```
```bash
docker-compose up --build fastapi_tests
```

### 5. Access the Services

After the services are running, you can access the different parts of the application as follows:

#### LLM FastAPI
- **URL**: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- This service handles the AI-generated content for the application.

#### Flask Backend
- **URL**: [http://127.0.0.1:5000](http://127.0.0.1:5000)
- This is the main backend that handles user authentication, workout and meal plans, and other business logic.

#### React Frontend
- **URL**: [http://127.0.0.1:3000](http://127.0.0.1:3000)
- This is the user-facing front-end where users interact with the application.

#### pgAdmin (Database Management)
- **URL**: [http://127.0.0.1:5050](http://127.0.0.1:5050)
- **Login Details**: Use the email and password set in the `.env` file (e.g., `PGADMIN_DEFAULT_EMAIL` and `PGADMIN_DEFAULT_PASSWORD`).
- **Connecting to Databases**: Once logged in, you can connect to the PostgreSQL databases:
  - **Flask Database**: 
    - Host: `flask_db_service`
    - Port: `5432`
    - Username: set in `.env` (`FLASK_DB_USER`)
    - Password: set in `.env` (`FLASK_DB_PASSWORD`)
    - Database: set in `.env` (`FLASK_DB_NAME`)
  - **FastAPI Database**: 
    - Host: `fastapi_db_service`
    - Port: `5434`
    - Username: set in `.env` (`FASTAPI_DB_USER`)
    - Password: set in `.env` (`FASTAPI_DB_PASSWORD`)
    - Database: set in `.env` (`FASTAPI_DB_NAME`)

#### Log into Each Database's CLI
You can access each PostgreSQL database directly via the command line interface (CLI). This can be useful for running manual queries, troubleshooting, or inspecting the database.

- **Flask Database**  

To log into the Flask database's CLI, run the following command:

```bash
docker exec -it flask_db_service psql -U $FLASK_DB_USER -d $FLASK_DB_NAME
```
This will open the PostgreSQL interactive terminal (psql) within the flask_db_service container.
It will automatically use the user and database set up in your .env file (FLASK_DB_USER and FLASK_DB_NAME).


- **FastAPI Database**

To log into the FastAPI database's CLI, run the following command:

```bash
docker exec -it fastapi_db_service psql -U $FASTAPI_DB_USER -d $FASTAPI_DB_NAME
```

This command does the same thing as above, but for the fastapi_db_service container.
It uses the credentials set in your .env file (FASTAPI_DB_USER and FASTAPI_DB_NAME).


- **Exit the CLI**

Once logged into the PostgreSQL CLI, you can run SQL commands directly. To exit the PostgreSQL interactive terminal, simply type:

```bash
\q
```

These instructions will allow you to access the CLI for each database service running in your Docker containers. Make sure that the corresponding containers are up and running before trying to log in.

### 6. Access the code

The project is organized into three main components: `fastapi_app`, `flask_app`, and `react_app`. Here's how to access and work with the code in each of these directories.

#### **FastAPI Application**
The `fastapi_app` directory contains the backend code for the FastAPI service.
- **Location:** `fastapi_app/`
- **Entry Point:** `fastapi_app/app.py`
- **Dockerfile:** You can find the Dockerfile for this service in `fastapi_app/Dockerfile-fastapi`.
- **Tests:** Tests for the FastAPI service are located in `fastapi_app/tests/`.

To make changes to the FastAPI application, edit the `app.py` file or other files as needed within the `fastapi_app/` directory.

To build and test changes:
```bash
docker-compose up --build fastapi_app
docker-compose up --build fastapi_tests
```

#### **Flask Application**
The flask_app directory contains the backend code for the Flask service.

- **Location:** `flask_app/`
- **Entry Point:** `flask_app/app.py`
- **Dockerfile:** You can find the Dockerfile for this service in `flask_app/Dockerfile-flask`.
- **Tests:** Tests for the Flask service are located in `flask_app/tests/`.
- To make changes to the Flask application, edit the `app.py` file or other files as needed within the `flask_app/` directory.

To build and test changes:

```bash
docker-compose up --build flask_app
docker-compose up --build flask_tests
```

#### **React Frontend**
The react_app directory contains the frontend code built with React.

- **Location:** `react_app/`
- **Entry Point:** `react_app/src/index.js`
- **Dockerfile:** You can find the Dockerfile for this service in `react_app/Dockerfile-react`.
- The `public/` directory contains static assets, while the `src/` directory contains the JavaScript and React component files. To make changes to the frontend, edit the files within the `src/` directory.

To build and test changes:

```bash
docker-compose up --build react_app
```


### 7. Stopping the Services

To stop all running services, press `Ctrl + C` in the terminal window running Docker. Alternatively, you can stop the services by running:

```bash
docker-compose down
```
