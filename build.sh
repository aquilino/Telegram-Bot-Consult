#!/bin/bash

docker-compose down && \
docker build -t h1dr0/bot:amd64 . && \
docker-compose -f docker-compose.yml -f docker-compose.caddy.yml up -d && \
docker-compose logs -f
