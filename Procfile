web: gunicorn school_transport.wsgi:application
release: python manage.py migrate --no-input && python manage.py create_admin
