import os
from unittest import mock
from django.conf import settings
from django.test import SimpleTestCase
from config.test import import_module



class SettingsTests(SimpleTestCase):
    def test_production_inactive(self):
        self.assertFalse(settings.CSRF_COOKIE_SECURE)
        self.assertEqual(settings.SECURE_HSTS_SECONDS, 0)

