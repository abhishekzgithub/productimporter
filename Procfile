web: gunicorn productimporter.wsgi --log-file -
worker: celery -A productimporter worker -l info -P eventlet
beat: python manage.py productimporter beat –loglevel=info

