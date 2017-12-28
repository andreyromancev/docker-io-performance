#!/bin/bash

trap exit 1 SIGINT SIGTERM

echo 'RUNNING FROM HOST ========================================='
python test.py

echo 'RUNNING FROM DOCKER ======================================='
docker build --rm -t docker-performance-test . &> /dev/null
docker run --rm -u $UID -v `pwd`:/var/app docker-performance-test
