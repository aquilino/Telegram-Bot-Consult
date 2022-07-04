#!/bin/bash

docker-compose down && \
docker build -t h1dr0/bot:amd64 . && \
docker-compose up -d && \
docker-compose logs -f
