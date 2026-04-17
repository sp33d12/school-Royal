"""
Creates a superuser from environment variables.
Safe to run multiple times — skips if the user already exists.
"""
import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Creates a superuser from DJANGO_SUPERUSER_* env vars if it does not exist'

    def handle(self, *args, **options):
        User = get_user_model()
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL', '')

        if not username or not password:
            self.stdout.write(self.style.WARNING(
                'Skipping admin creation — DJANGO_SUPERUSER_USERNAME or DJANGO_SUPERUSER_PASSWORD not set'
            ))
            return

        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.WARNING(
                f'Admin user "{username}" already exists — skipping creation'
            ))
            return

        User.objects.create_superuser(username=username, email=email, password=password)
        self.stdout.write(self.style.SUCCESS(
            f'✓ Admin user "{username}" created successfully!'
        ))
