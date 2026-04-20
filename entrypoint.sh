#!/bin/sh
set -e

python manage.py makemigrations student
python manage.py migrate

exec gunicorn core.wsgi:application --bind 0.0.0.0:8000
