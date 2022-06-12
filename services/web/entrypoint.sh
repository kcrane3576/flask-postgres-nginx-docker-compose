#!/bin/sh
# Verify Postgres is up and healthy
# Note: File permissions requirement
# - chmod +x services/web/entrypoint.sh
if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py create_db
python manage.py seed_db

exec "$@"