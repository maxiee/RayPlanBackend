#!/bin/sh

git pull

docker-compose -f docker-compose.prod.yml down -v

docker-compose -f docker-compose.prod.yml up -d --build

docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput

