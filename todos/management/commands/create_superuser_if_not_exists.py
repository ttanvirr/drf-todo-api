import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Create admin superuser if DJANGO_SUPERUSER_PASSWORD is set"

    def handle(self, *args, **options):
        password = os.getenv("DJANGO_SUPERUSER_PASSWORD")

        if not password:
            self.stdout.write("DJANGO_SUPERUSER_PASSWORD not set")
            return

        User = get_user_model()

        if User.objects.filter(username="admin").exists():
            self.stdout.write("Admin user already exists")
            return

        User.objects.create_superuser(
            username="admin",
            email="admin@email.com",
            password=password,
        )

        self.stdout.write(self.style.SUCCESS("Admin superuser created"))
