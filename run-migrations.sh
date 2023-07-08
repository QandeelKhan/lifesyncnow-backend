#!/bin/bash
set -e

# Uncomment the following lines if you want to wait for the database to start
# echo "Waiting for database to start..."
# until PGPASSWORD=$POSTGRES_PASSWORD psql -h "db" -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c '\q'; do
#     echo >&2 "Postgres is unavailable - sleeping"
#     sleep 1
# done
# echo "Postgres is up - running migrations...."
# RUN BACKUP RESTORE
# docker-compose -f docker-compose.prod.yml exec -T lifesyncnow-db psql -U postgres -d postgres < ./lifesyncnow_db_backup.sql
# pg_restore -U postgres -d postgres <./lifesyncnow_db_backup.sql
# echo "Backup restored successfully...!"
# Run migrations
# python manage.py collectstatic --noinput --clear (will siilently remove any existing static files to the aws or django project folder if it already exist, to save from overwritting)
# python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py makemigrations user_management
python manage.py migrate user_management
python manage.py makemigrations blog user_profile subscriber page global_content legal
python manage.py migrate
echo "Migrations complete"

# Create a background process for gunicorn server
gunicorn lifesyncnow_backend.wsgi:application --env DJANGO_SETTINGS_MODULE=lifesyncnow_backend.settings.dev --bind 0.0.0.0:8000 --workers 2 --threads 2 &
# --workers 1 --threads 2 & (for single(core) cpu and 2gb ram)
# Store the background process ID
gunicorn_pid=$!

# Uncomment the following line if you want to run the Django server using 'python manage.py runserver'
# python manage.py runserver

# Wait for the gunicorn server to complete before exiting the script
wait $gunicorn_pid
