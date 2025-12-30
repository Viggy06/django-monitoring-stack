# Django Monitoring Stack (Django-RestAPIs) + Prometheus + Grafana)
  This project is fully functional Rest API for managing student apis with monitoring observality, built with django, grafana, prometheus
## 🚀 Features

  ### 🔹 Django REST API
    - Full **CRUD functionality** (Create, Read, Update, Delete) for student records
    - Built using **Django** and **Django REST Framework**
    - Served via **Gunicorn** for production readiness
    
  ### 🔹 Database
    - Uses **SQLite** for quick setup and ease of development

  ### 🔹 Observability & Monitoring
    - **Prometheus**
      - Collects metrics from the Django application (`/metrics`)
      - Scrapes host-level metrics via Node Exporter
    - **Grafana**
      - Visualizes application and system metrics
      - Supports dashboards for Django and Node Exporter
      
  ### 🔹 Containerization
    -  Fully containerized with Docker and Docker Compose for easy setup and consistent development environments.

# Prerequisites
  -  [Docker](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)

# Installation and Setup
  1. Clone the repository:
    git clone <your-repository-url>
    cd django-monitoring-stack
  2. Now run docker compose command
    docker compose up -d --build
    you can check running container using command - docker ps
  3. To configure prometheus with grafana follow the screenshot given - 
      
# Usage
  We can interact with the API using any HTTP client. A Postman collection is included in the repository (student-api.postman_collection.json) for the convenience.
  ## API Endpoints

| Method | Endpoint                   | Description                   |
|-------:|----------------------------|-------------------------------|
| POST   | /api/v1/students           | Creates a new student         |
| GET    | /api/v1/students           | Lists all students            |
| GET    | /api/v1/students/{id}      | Retrieves a single student    |
| PUT    | /api/v1/students/{id}      | Updates an existing student   |
| DELETE | /api/v1/students/{id}      | Deletes a student             |

# Viewing Observability Data
  - Navigate to http://localhost:3000(grafana-UI) to explore system resources, metrics and logs for the application

