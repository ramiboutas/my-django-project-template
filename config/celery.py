from __future__ import annotations

import os

from celery import Celery
from celery.schedules import crontab
from django.apps import apps
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")


app = Celery("config")
app.config_from_object(settings, namespace="CELERY")
app.conf.timezone = settings.TIME_ZONE
app.autodiscover_tasks()
app.conf.beat_schedule = {
    "my_task": {
        "task": "myapp.tasks.my_task",
        "schedule": crontab(hour="10, 15", minute=00),
        "options": {
            "expires": 0,
        },
    },
}
