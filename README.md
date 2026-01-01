# Django Monitoring Stack (Django-RestAPIs + Prometheus + Grafana)
  This project is fully functional Rest API for managing student apis with monitoring observality, built with django, grafana, prometheus
## 🚀 Features

  ### 🔹 Django REST API
    - Fully **CRUD functionality** (Create, Read, Update, Delete) for student records
    - Built using **Django** and **Django REST Framework**
    - Served via **Gunicorn** for production readiness
    
  ### 🔹 Database
    - Uses **SQLite** for quick setup and ease of development

  ### 🔹 Observability & Monitoring
    **Prometheus**
      - Collects metrics from the Django application (`/metrics`)
      - Scrapes host-level metrics via Node Exporter
    **Grafana**
      - Visualizes application and system metrics
      - Supports dashboards for Django and Node Exporter
      
  ### 🔹 Containerization
    -  Fully containerized with Docker and Docker Compose for easy setup and consistent development environments.

# Prerequisites
  -  [Docker](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)

# Installation and Setup
  1. Clone the repository:
    ```
      git clone <your-repository-url>
      cd django-monitoring-stack
    ```
  2. Give sudo permission to docker group and user, using this command user will not need to call sudo for using docker.
    ```
      usermod -aG docker ubuntu
      newgrp docker
    ```
  3. Now run docker compose command
    ```
      docker compose up -d --build
      you can check running container using command - docker ps
    ```
  4. You need to add data source and dashboard for node-exporter and django api 
     To configure this in grafana follow the steps given -
    
      1. Create your username and password 
       <img width="1909" height="906" alt="grafana_1" src="https://github.com/user-attachments/assets/640ec852-36b5-4815-882e-469afd95d521" />
      2. After login into the grafana click on **Connection** then **Data sources** and serach for prometheus
        <img width="1909" height="909" alt="grafana_3" src="https://github.com/user-attachments/assets/fd69bb33-f674-431b-9239-ff1f8be4732c" />
      3. 


    
      
  
      
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
  - Navigate to http://localhost:3000/ (grafana-UI)) and http://localhost:9090 (prometheus-ui) to explore system resources, metrics and logs for the application

# To stress test
  We will use stress-

# Screenshots from my implemented project
  Prometheus Configured
  <img width="1916" height="648" alt="prometheus-configured-ui" src="https://github.com/user-attachments/assets/c5937caf-bf33-43dc-b563-30d26097fec7" />

  Node-exporter Configured
  <img width="1916" height="648" alt="node-exporter-configured-ui" src="https://github.com/user-attachments/assets/7ada4ff7-b0e7-4e25-b121-ece111809abe" />
  
  Django-Metrics exposed using django-prometheus
  <img width="1885" height="648" alt="django-metrics-exposed" src="https://github.com/user-attachments/assets/71c9af27-a7ec-4982-a47b-4f445719ca97" />

  Django-Apis-Monitoring-Dashboard
  <img width="1883" height="944" alt="django-apis-monitoring-dashboard" src="https://github.com/user-attachments/assets/ac5a7b9c-b36d-48e8-8f58-314b8744e666" />

  Grafana Dashboard with system metrics
  <img width="1884" height="819" alt="grafana-stress-test-ss" src="https://github.com/user-attachments/assets/42f5f01e-d751-4edc-8ad8-b414ae7e9cd1" />

  

