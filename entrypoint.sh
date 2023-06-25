#!/bin/bash
set -e

# Start the PostgreSQL service
service postgresql start

# Run any database migrations
python manage.py collectstatic --noinput
python manage.py makemigrations UserManagement
python manage.py migrate UserManagement
python manage.py makemigrations UserProfile
python manage.py migrate UserProfile
python manage.py makemigrations blog
python manage.py migrate blog
python manage.py makemigrations ContactUs
python manage.py migrate ContactUs
python manage.py makemigrations PageTemplate
python manage.py migrate PageTemplate
python manage.py makemigrations Subscriber
python manage.py migrate Subscriber
python manage.py migrate

# Start the Django server, runs the default CMD command specified in the Dockerfile.
exec "$@"
