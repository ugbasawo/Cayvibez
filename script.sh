#!/usr/bin/env bash
export IMAGE_NAME_1=$1
export IMAGE_NAME_2=$2
export IMAGE_NAME_3=$3
export IMAGE_NAME_4=$4
export IMAGE_NAME_5=$5
docker pull rabbitmq:management-alpine
docker pull ${IMAGE_NAME_1}
docker pull ${IMAGE_NAME_2}
docker pull ${IMAGE_NAME_3}
docker pull ${IMAGE_NAME_4}
# docker pull ${IMAGE_NAME_5}
docker compose -f docker-compose.yml up -d