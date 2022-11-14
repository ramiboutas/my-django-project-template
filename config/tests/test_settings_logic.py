from __future__ import annotations

import os
from unittest.mock import patch

from django.conf import settings
from django.test import modify_settings
from django.test import override_settings
from django.test import TestCase


class SettingsTests(TestCase):
    def test_production_inactive(self):
        self.assertFalse(settings.CSRF_COOKIE_SECURE)
        self.assertEqual(settings.SECURE_HSTS_SECONDS, 0)

    def test_not_use_postgres(self):
        self.assertEqual(
            settings.DATABASES["default"]["ENGINE"], "django.db.backends.sqlite3"
        )
