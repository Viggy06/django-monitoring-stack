# Django Monitoring Stack (Django-RestAPIs + Prometheus + Grafana)
  This project is fully functional Rest API for managing student apis with monitoring observality, built with django, grafana, prometheus
##  Features
- **CRUD REST API**
  - Full CRUD functionality (Create, Read, Update, Delete) for student records
  - Built using **Django REST Framework**
- **Database**
  - We will use **PostgresSQL** DB for storing data.
- **Observability & Monitoring**
  - **Prometheus**
    - Collects metrics from the Django application (`/metrics`)
    - Scrapes host-level metrics via Node Exporter
  - **Grafana**
    - Visualizes application and system metrics
    - Supports dashboards for Django and Node Exporter
- **Containerization**
  - Fully containerized using **Docker** and **Docker Compose**
  
## Prerequisites
  -  [Docker](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)

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
  
## Installation and Setup
  1. ***Clone the repository:***
      ```bash
       git clone <your-repository-url>
       cd django-monitoring-stack
     ```
  2. ***Configure Environment***: Create a .env file by copying the provided dummy file. The default values are configured to work with the Docker Compose setup.
       ```bash
          cp .env.dummy .env
       ```
  3. ***Adding a user to the docker group allows them to run Docker without sudo.***
      ```bash
        sudo usermod -aG docker ubuntu
        newgrp docker
      ```
  4. ***Now run docker compose command***
      ```bash
        docker compose up -d --build
        docker ps
      ```
  5. ***We need to add data source and dashboard for node-exporter and django api. To configure this in grafana follow the steps given -***
    
      1. Create username and password
         <img width="1909" height="906" alt="grafana_1" src="https://github.com/user-attachments/assets/640ec852-36b5-4815-882e-469afd95d521" />
         
      2. After login into the grafana click on **Connection** then **Add new connection** and search for prometheus and click on it and select **Add new data   source**
         <img width="1919" height="863" alt="image" src="https://github.com/user-attachments/assets/a0eb750a-cdd8-4c1e-a628-753b85d4dcc2" />
         <img width="1887" height="911" alt="image" src="https://github.com/user-attachments/assets/97b767f2-18b5-48e3-af63-cfa7c01b73d4" />

      3. Scroll-down to connection and add server url
         <img width="1917" height="529" alt="image" src="https://github.com/user-attachments/assets/08016020-f04a-420b-bb7f-2973b8151198" />
        
      4. Then scroll-down further and click on **Save & Test**, if this message comes **Successfully queried the Prometheus API.** it means configuration is working
         <img width="1858" height="879" alt="image" src="https://github.com/user-attachments/assets/ea96a74b-894e-44dd-987d-0e768e37f1db" />
      
      5. Now we should able to see Prometheus in Data sources
         <img width="1905" height="623" alt="image" src="https://github.com/user-attachments/assets/37803a37-bd0e-478e-8617-49fe7d3d3861" />
      
      6. To configure Node-exporter and Django API dashboards we need to import the dashboard.Select ***Create Dashboard***
          <img width="1911" height="954" alt="grafana_5" src="https://github.com/user-attachments/assets/d3a1e4b9-14d3-470e-ab13-ae3d321b3e52" />
          Then ***Import Dashboard***
          <img width="1887" height="899" alt="image" src="https://github.com/user-attachments/assets/a6e3ad68-b9d4-4524-ba85-d450d7283833" />
          Import Dashboard Json file or Add Dasboard then click on Import
          <img width="1746" height="882" alt="image" src="https://github.com/user-attachments/assets/a4a93f25-20f2-4140-8e15-5152cee65545" />
          <img width="1913" height="912" alt="image" src="https://github.com/user-attachments/assets/be976d94-ebd6-4cc6-970a-d256d07f64a9" />
          Follow the same step to add django api dashboard with Dashboard ID **17658**

# Screenshots from my implemented project
  ### Prometheus Configured
  <img width="1916" height="648" alt="prometheus-configured-ui" src="https://github.com/user-attachments/assets/c5937caf-bf33-43dc-b563-30d26097fec7" />

  ### Prometheus-Targets
  <img width="1910" height="908" alt="prometheus-targets" src="https://github.com/user-attachments/assets/1191d412-598f-4f0d-bd64-a6ac394e8241" />

  ### Node-exporter Configured
  <img width="1916" height="648" alt="node-exporter-configured-ui" src="https://github.com/user-attachments/assets/7ada4ff7-b0e7-4e25-b121-ece111809abe" />

  ### Django-Metrics exposed using django-prometheus
  <img width="1885" height="648" alt="django-metrics-exposed" src="https://github.com/user-attachments/assets/71c9af27-a7ec-4982-a47b-4f445719ca97" />

  ### Django-Apis-Monitoring-Dashboard
  <img width="1883" height="944" alt="django-apis-monitoring-dashboard" src="https://github.com/user-attachments/assets/ac5a7b9c-b36d-48e8-8f58-314b8744e666" />

  ### Grafana Dashboard with system metrics
  <img width="1884" height="819" alt="grafana-stress-test-ss" src="https://github.com/user-attachments/assets/42f5f01e-d751-4edc-8ad8-b414ae7e9cd1" />

  

