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

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/nexfitra.git
   cd nexfitra
    ```
2. **Install dependencies using Poetry:**
    ```bash
    poetry install
    ```
3. **Run Docker Compose for development:**
    ```bash
    docker-compose up --build
    ```
4. **Access the app:**
- Frontend: http://localhost:3000
- Flask Backend: http://localhost:5000
- FastAPI AI Service: http://localhost:8000

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
