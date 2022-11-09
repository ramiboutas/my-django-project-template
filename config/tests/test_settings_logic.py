from __future__ import annotations

from django.conf import settings
from django.test.utils import override_settings
from django.test import SimpleTestCase


class SettingsTests(SimpleTestCase):
    def test_production_inactive(self):
        self.assertFalse(settings.CSRF_COOKIE_SECURE)
        self.assertEqual(settings.SECURE_HSTS_SECONDS, 0)
    
    def test_not_use_postgres(self):
        self.assertEqual(
            settings.DATABASES["default"]["ENGINE"],
             "django.db.backends.sqlite3"
             )

    def test_use_postgres(self):
        self.assertEqual(
            settings.DATABASES["default"]["ENGINE"],
             "django.db.backends.postgresql"
             )
