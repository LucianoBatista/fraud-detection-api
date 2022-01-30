#!/bin/sh
if [ "${DYNO}" = 'worker' ]; then
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

    gunicorn --bind 0.0.0.0:$PORT manage:app

fi
