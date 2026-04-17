"""
Creates a superuser from environment variables.
Safe to run multiple times — skips if the user already exists.
"""
import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

# Static additional usernames to include in repo (sanitized: spaces replaced with underscores)
STATIC_ADDITIONAL_USERS = [
    "manger_ali",
    "it_mohammad",
]


class Command(BaseCommand):
    help = (
        'Creates a superuser from DJANGO_SUPERUSER_* env vars if it does not exist. '
        'Supports additional users via DJANGO_SUPERUSER_ADDITIONAL or static list when '
        'DJANGO_SUPERUSER_CREATE_STATIC=1.'
    )

    def create_user_if_missing(self, User, username, email, password, force_reset=False):
        if not username or not password:
            self.stdout.write(self.style.WARNING(
                f'Skipping admin creation — username or password not set for "{username}"'
            ))
            return False
        
        existing = User.objects.filter(username=username).first()
        
        if existing and force_reset:
            # Delete and recreate with new password
            existing.delete()
            self.stdout.write(self.style.WARNING(
                f'Deleted existing user "{username}" (force reset)'
            ))
            existing = None
        
        if existing:
            self.stdout.write(self.style.WARNING(
                f'Admin user "{username}" already exists — skipping creation'
            ))
            return False
        
        User.objects.create_superuser(username=username, email=email or '', password=password)
        self.stdout.write(self.style.SUCCESS(
            f'✓ Admin user "{username}" created successfully!'
        ))
        return True

    def handle(self, *args, **options):
        User = get_user_model()
        force_reset = os.environ.get('DJANGO_SUPERUSER_RESET', '0') == '1'

        # Primary admin (legacy behavior)
        username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL', '')

        if username and password:
            self.create_user_if_missing(User, username, email, password, force_reset=force_reset)
        else:
            self.stdout.write(self.style.WARNING(
                'Skipping primary admin creation — DJANGO_SUPERUSER_USERNAME or DJANGO_SUPERUSER_PASSWORD not set'
            ))

        # Additional admin users from DJANGO_SUPERUSER_ADDITIONAL (format: user[:email],user2[:email2])
        additional = os.environ.get('DJANGO_SUPERUSER_ADDITIONAL', '')
        if additional:
            passwords_env = os.environ.get('DJANGO_SUPERUSER_PASSWORDS')  # optional comma separated passwords
            pw_list = [p.strip() for p in passwords_env.split(',')] if passwords_env else None
            entries = [e.strip() for e in additional.split(',') if e.strip()]
            for i, entry in enumerate(entries):
                parts = entry.split(':', 1)
                uname = parts[0].strip().replace(' ', '_')
                uemail = parts[1].strip() if len(parts) > 1 else ''
                pw = pw_list[i] if pw_list and i < len(pw_list) else password
                if not pw:
                    self.stdout.write(self.style.WARNING(
                        f'Skipping additional admin "{uname}" — no password available'
                    ))
                    continue
                self.create_user_if_missing(User, uname, uemail, pw, force_reset=force_reset)

        # Static additional users defined in code (only created when DJANGO_SUPERUSER_CREATE_STATIC=1)
        create_static = os.environ.get('DJANGO_SUPERUSER_CREATE_STATIC', '0') == '1'
        if create_static:
            for uname in STATIC_ADDITIONAL_USERS:
                uname_sanitized = uname.replace(' ', '_')
                pw = password
                if not pw:
                    self.stdout.write(self.style.WARNING(
                        f'Skipping static admin "{uname_sanitized}" — DJANGO_SUPERUSER_PASSWORD not set'
                    ))
                    continue
                self.create_user_if_missing(User, uname_sanitized, '', pw, force_reset=force_reset)
