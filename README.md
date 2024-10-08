# NexFitra

## Project Overview
NexFitra is a health and fitness app that helps users create and track personalized workout schedules and meal plans. It leverages a generative AI model to provide customized plans based on user inputs.

## Technology Stack
- **Frontend**: React
- **Backend**: Flask and FastAPI
- **Database**: PostgreSQL
- **Orchestration**: Kubernetes
- **Containerization**: Docker
- **Dependency Management**: Poetry

## Setup Instructions

For detailed setup instructions, please see the [setup guide](docs/setup/setup.md).

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

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
