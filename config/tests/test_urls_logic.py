from pickle import TRUE
from django.conf import settings
from django.test import SimpleTestCase, override_settings
from django.conf.urls.static import static

from config.urls import urlpatterns

class UrlsTests(SimpleTestCase):
    def test_debug_inactive(self):
        static_url = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        media_url = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        static_url_included = static_url in urlpatterns
        media_url_included = media_url in urlpatterns
        self.assertFalse(static_url_included)
        self.assertFalse(media_url_included)
