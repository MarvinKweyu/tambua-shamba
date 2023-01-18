FROM python:3.10-alpine

#  working directory for docker instructions
WORKDIR /app

#  set environment variables
ENV PYTHONUNBUFFERED=1  WEB_CONCURRENCY=3
# prevent python from buffering stdout and stderr
ENV PYTHONBUFFERED 1
# fix cryptography package errors
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1

# install psycopg2 dependencies
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev


# install dependencies
RUN pip3 install --upgrade pip
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt


# copy entrypoint.sh
COPY ./entrypoint.sh .

# COPY PROJECT
COPY . .

# run entrypoint.sh
ENTRYPOINT [ "/app/entrypoint.sh" ]
