# Tambua Shamba

> A project to collect and preview soil organic carbon performance in farms across Kenya 


## Table of Contents
- [Tambua Shamba](#grow-everything)
  - [Table of Contents](#table-of-contents)
  - [Running TambuaShamba Locally](#running-groweverything-locally)
    - [Manual Setup](#manual-setup)
    - [Docker Setup](#docker-setup)
  - [Production Day](#production-day)
  - [Project path and improvements](#project-path-and-improvements)

## Running TambuaShamba Locally

Create a `.env.dev` file at the root directory and copy contents of the `.env.example` file to it. Modify where necessary.

### Manual Setup

**Basic system requirements**

Ensure you have the following packages installed and set up.

 - Postgres
 - PostGIS

Create a database and modify the `env*` file with the appropriate db details included.

Create a python virtual environment, install the dependencies and run the migrations.

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
### Docker Setup
**Basic requirements**
  - Docker
  - Docker-compose

To run the project, navigate to the root and run the below:
```bash
docker-compose up -d --build
```
Access the project documentation on your local machine on **http://127.0.0.1:8000/api/v1/redoc/** 
## Production Day

The  following are the steps you might need to do to set this up on production:

- Create a file `.env.prod` to contain production variables at the root of the project.
- Generate a new secret key for production environments
- Add the local environment variables to it while changing the allowed hosts, database details and any other information used on your production environment.

## Project path and improvements
- Add authentication for specific users to access the resources.

- Intergration of asynchronous tasks. 
  Use celery and rabbitMQ to update farms from the CSV asynchronously.