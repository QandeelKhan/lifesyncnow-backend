#!/bin/bash
set -e

# echo "Waiting for database to start..."

# Wait for the database to start before running migrations
# until PGPASSWORD=$POSTGRES_PASSWORD psql -h "db" -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c '\q'; do
#     echo >&2 "Postgres is unavailable - sleeping"
#     sleep 1
# done

# echo "Postgres is up - running migrations...."

# Run migrations
python manage.py collectstatic --noinput
python manage.py makemigrations UserManagement
python manage.py migrate UserManagement
python manage.py makemigrations blog
python manage.py migrate blog
python manage.py migrate
echo "Migrations complete"
echo "running our django server"
python manage.py runserver 0.0.0.0:8000
