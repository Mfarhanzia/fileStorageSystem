web: gunicorn spekit_assignment.wsgi --log-file -
release: python manage.py migrate --no-input
release: python manage.py loaddata folder.json
release: python manage.py loaddata topics.json

