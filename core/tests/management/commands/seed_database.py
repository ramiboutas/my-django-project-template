import random

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand
from django.core.management.base import CommandError
from django.db import transaction

from core.models import Example

User = get_user_model()


class Command(BaseCommand):
    help = "Seed database with sample data."

    @transaction.atomic
    def handle(self, *args, **options):
        if Example.objects.exists() or not settings.DEBUG:
            raise CommandError(
                "This command cannot be run when any authors exist, to guard "
                + "against accidental use on production."
            )

        self.stdout.write("Seeding database...")

        update_site()

        create_objects()

        self.stdout.write("Done.")


def update_site():
    domain = "localhost:8000"
    Site.objects.filter(domain="example.com").update(domain=domain, name=domain)


def create_objects():
    example_names = [f"Example {i}" for i in range(1, 6)]

    Example.objects.bulk_create([Example(name=name) for name in example_names])

    User.objects.create_superuser(
        username="admin",
        email="admin@example.com",
        password="admin",
    )

    # to do
    # make a custom check to make sure that on production there no user called admin
