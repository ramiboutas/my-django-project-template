from __future__ import annotations

import os

from celery import Celery
from django.apps import apps
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("config")
app.config_from_object(settings, namespace="CELERY")
app.conf.timezone = settings.TIME_ZONE
app.autodiscover_tasks(lambda: [n.name for n in apps.get_app_configs()])


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
