# Grow Everything

> A project to collect and preview soil organic carbon performance in farms across Kenya 



## Table of Contents
- [Grow Everything](#grow-everything)
  - [Table of Contents](#table-of-contents)
  - [Running GrowEverything Locally](#running-groweverything-locally)
    - [Manual Setup](#manual-setup)
    - [Docker Setup(WIP)](#docker-setupwip)
  - [Production Day](#production-day)
  - [Project path and improvements](#project-path-and-improvements)


## Running GrowEverything Locally

### Manual Setup

Create a python virtual environment, install the dependencies and run the migrations
```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
python3 manage.py runserver
```

Run the server
```bash
python3 manage.py runserver
```
### Docker Setup(WIP)
With docker installed on your host machine, perform the following operations.
Ensure you have both docker and docker -compose installed

Clone the application, navigate to the root directory, build the image, run it in detached mode and run migrations

```bash

docker-compose up -d --build
docker-compose exec web python3 manage.py migrate --settings=grow_everything.settings.dev --noinput

```

## Production Day

With dockers
## Project path and improvements

- Intergration of asynchronous tasks
  * Update farms from the CSV asynchronously. Use celery and rabbitMQ for this.
  * 