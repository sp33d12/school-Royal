#!/usr/bin/env bash
# Render build script — runs during every deploy.
# Installs dependencies, collects static files, runs migrations, creates admin.

set -o errexit  # Exit on any error

echo "==> Installing Python dependencies"
pip install -r requirements.txt

echo "==> Collecting static files"
python manage.py collectstatic --no-input

echo "==> Running database migrations"
python manage.py migrate --no-input

echo "==> Creating admin user (if not exists)"
python manage.py create_admin

echo "==> Build complete!"

