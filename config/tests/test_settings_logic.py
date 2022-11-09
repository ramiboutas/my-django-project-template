from __future__ import annotations
import os
from django.conf import settings
from django.test import TestCase, override_settings, modify_settings
from unittest.mock import patch

class SettingsTests(TestCase):
    def test_production_inactive(self):
        self.assertFalse(settings.CSRF_COOKIE_SECURE)
        self.assertEqual(settings.SECURE_HSTS_SECONDS, 0)
    
    def test_not_use_postgres(self):
        self.assertEqual(
            settings.DATABASES["default"]["ENGINE"],
             "django.db.backends.sqlite3"
             )
