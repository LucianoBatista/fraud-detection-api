#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z api-db 5432; do
    sleep 0.1
done

echo "PostgreSQL started"

if [ "${APP_NAME}" = 'worker' ]; then
    echo 'Starting Worker'

    celery \
        -A src.celery worker \
            -l 'INFO' \
            -c "${WORKER_CONCURRENCY:-1}" \
            -E \
            --without-gossip \
            --without-mingle \
            --without-heartbeat
else
    echo 'Starting Flask Web Application...'

    flask db upgrade
    python manage.py seed_model
    python manage.py seed_predict
    python manage.py seed_training
    python manage.py run -h 0.0.0.0 

fi
