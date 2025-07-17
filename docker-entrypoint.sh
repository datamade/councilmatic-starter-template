#!/bin/sh
set -e

pip install "pip<24.1" && pip install -e /app/django-councilmatic[all]

if [ "$DJANGO_MANAGEPY_MIGRATE" = 'on' ]; then
    python manage.py migrate --noinput
fi


exec "$@"
