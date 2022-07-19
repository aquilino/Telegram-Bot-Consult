#!/bin/bash

echo -e "\t\n[*] ejemplo -> ./build.sh caddy "

read a

docker-compose down && \
docker build -t h1dr0/bot:amd64 . && \
docker-compose -f docker-compose.yml -f docker-compose.$a.yml up -d && \
docker-compose logs -f
