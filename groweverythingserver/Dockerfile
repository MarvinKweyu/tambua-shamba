FROM python:3.10-slim-buster

LABEL maintainer="hello@marvinkweyu.net"
LABEL description="Grow Everything product for soil carbon mapping in Kenya"

#  working directory for docker instructions
WORKDIR /app

#  set environment variables
ENV PYTHONUNBUFFERED=1  WEB_CONCURRENCY=3
# prevent python from buffering stdout and stderr
ENV PYTHONBUFFERED 1
# fix cryptography package errors
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1

RUN apt-get update && apt-get -y install netcat gcc postgresql && apt-get clean

RUN apt-get update \
    && apt-get install -y binutils libproj-dev gdal-bin python-gdal python3-gdal postgis
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