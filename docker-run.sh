###############
# Run the gunicorn docker image process.
###############
cd /app
LOG_LEVEL=$([ "$NODE_ENV" = "staging" ] && echo "debug" || echo "info")
exec gunicorn app:app -t 30 --workers ${NUM_WORKERS-'4'} --bind=0.0.0.0:${GUNICORN_APP_PORT-'5000'} --log-level $LOG_LEVEL --log-file=-