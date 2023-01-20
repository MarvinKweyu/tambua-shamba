# Grow Everything

> A project to collect and preview soil organic carbon performance in farms across Kenya 


## Table of Contents
  - [Running GrowEverything Locally](#running-groweverything-locally)
    - [Manual Setup](#manual-setup)
    - [Docker Setup(WIP)](#docker-setupwip)
  - [Production Day](#production-day)
  - [Project path and improvements](#project-path-and-improvements)


## Running GrowEverything Locally

### Manual Setup

**Basic system requirements**

Ensure you have the following packages installed and set up.

 - Postgres
 - PostGIS


Create a python virtual environment, install the dependencies and run the migrations
```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

Run the server
```bash
python3 manage.py runserver
```

Access the project documentation on your local machine on **http://127.0.0.1:8000/api/v1/redoc/** 
### Docker Setup(WIP)
**Basic requirements**
  - Docker
  - Docker-compose

To run the project
```bash
docker-compose up -d --build
```
Access the project documentation on your local machine on **http://127.0.0.1:8000/api/v1/redoc/** 
## Production Day

Modify the allowed hosts variable to accept requests from the client of your choice.

## Project path and improvements
- Add authentication for specific users to access the resources.

- Intergration of asynchronous tasks. 
  Use celery and rabbitMQ to update farms from the CSV asynchronously.