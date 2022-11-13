from __future__ import annotations

import os
import sys
from pathlib import Path

import dotenv

# Setup

# Build paths inside the project like this: BASE_DIR / "subdir".
BASE_DIR = Path(__file__).resolve().parent.parent

# Load env vars from .env file if not testing
try:
    command = sys.argv[1]
except IndexError:  # pragma: no cover
    command = "help"

if command != "test":  # pragma: no cover
    dotenv.load_dotenv(dotenv_path=BASE_DIR / ".env")


# The name of the class to use for starting the test suite.
TEST_RUNNER = "config.test.TestRunner"

# Django secret key
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "some-tests-need-a-secret-key")

# Debug flag
DEBUG = os.environ.get("DEBUG", "") == "1"

# Use redis caching
USE_REDIS_CACHING = os.environ.get("USE_REDIS_CACHING", "") == "1"

# Use Postgres (otherwise SqLite)
USE_POSTGRES = os.environ.get("USE_POSTGRES", "") == "1"

# Use real email backend
USE_EMAIL_BACKEND = os.environ.get("USE_EMAIL_BACKEND", "") == "1"

# Use Digital Ocean Spaces service (Storage)
USE_SPACES = os.environ.get("USE_SPACES", "") == "1"

# https for production
HTTPS = os.environ.get("HTTPS", "") == "1"


INTERNAL_IPS = [
    "127.0.0.1",
    "localhost",
]

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
]

# Application definition

INSTALLED_APPS = [
    # My apps
    "core.apps.CoreConfig",
    # Third-party apps
    # Django contrib apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# Database
# https://docs.djangoproject.com/en/stable/ref/settings/#databases


if USE_POSTGRES:    # # pragma: no cover
    POSTGRES_DB = os.environ.get("POSTGRES_DB", "")
    POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "")
    POSTGRES_USER = os.environ.get("POSTGRES_USER", "")
    POSTGRES_HOST = os.environ.get("POSTGRES_HOST", "")
    POSTGRES_PORT = os.environ.get("POSTGRES_PORT", "")
    POSTGRES_TESTS_DB = os.environ.get("POSTGRES_TESTS_DB", "")

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": POSTGRES_DB,
            "USER": POSTGRES_USER,
            "PASSWORD": POSTGRES_PASSWORD,
            "HOST": POSTGRES_HOST,
            "PORT": POSTGRES_PORT,
            "TEST": {
                "NAME": "test_db",
            },
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }


# Password validation
# https://docs.djangoproject.com/en/stable/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/stable/topics/i18n/

LANGUAGE_CODE = "en-UK"

TIME_ZONE = "Europe/Berlin"

USE_I18N = True

USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/stable/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static_dev"),
]

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Third-party settings

# celery
CELERY_BROKER_URL = "redis://127.0.0.1:6379/4"
CELERY_RESULT_BACKEND = 'django-db'
CELERY_RESULT_EXTENDED = True


# Project Settings


# caching


if USE_REDIS_CACHING:   # pragma: no cover
    REDIS_CACHING_LOCATION = os.environ.get("REDIS_CACHING_LOCATION", "")
    CELERY_CACHE_BACKEND = "default"
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.redis.RedisCache",
            "LOCATION": REDIS_CACHING_LOCATION,
        }
    }
else:
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.dummy.DummyCache",
        }
    }


# SMTP Email
if USE_EMAIL_BACKEND:   # pragma: no cover
    EMAIL_HOST = os.environ.get("EMAIL_HOST")
    EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
    EMAIL_PORT_STR = os.environ.get("EMAIL_PORT")
    EMAIL_PORT = int(EMAIL_PORT_STR) if EMAIL_PORT_STR is not None else 1234
    EMAIL_USE_TLS = True
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

else:    # pragma: no cover
    EMAIL_USE_TLS = False
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"



if USE_SPACES:   # pragma: no cover
    # Stuff that could be useful (comments):
    # AWS_LOCATION = f'https://{AWS_STORAGE_BUCKET_NAME}.fra1.digitaloceanspaces.com'
    # MEDIA_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.fra1.digitaloceanspaces.com/{AWS_MEDIA_LOCATION}/' # it worked
    # MEDIA_URL = f'https://{AWS_s3_endpoint_url}/{AWS_MEDIA_LOCATION}/'
    # STATIC_URL = f'https://{AWS_s3_endpoint_url}/{AWS_STATIC_LOCATION}/'

    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

    AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
    AWS_S3_ENDPOINT_URL = "https://fra1.digitaloceanspaces.com"
    AWS_S3_CUSTOM_DOMAIN = (
        "ramiboutas.fra1.cdn.digitaloceanspaces.com"  # spaces.ramiboutas.com
    )
    AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400", "ACL": "public-read"}

    AWS_DEFAULT_ACL = "public-read"
    AWS_S3_SIGNATURE_VERSION = "s3v4"

    DEFAULT_FILE_STORAGE = "config.storage_backends.MediaRootStorage"
    STATICFILES_STORAGE = "config.storage_backends.StaticRootStorage"

    AWS_STATIC_LOCATION = "englishstuff-static"
    STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_STATIC_LOCATION}/"
    STATIC_ROOT = f"{AWS_STATIC_LOCATION}/"

    AWS_MEDIA_LOCATION = "englishstuff-media"

    MEDIA_URL = f"{AWS_S3_CUSTOM_DOMAIN}/{AWS_MEDIA_LOCATION}/"
    MEDIA_ROOT = f"{AWS_MEDIA_LOCATION}/"



if HTTPS:  # pragma: no cover
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_HSTS_SECONDS = 31_536_000  # 31536000 # usual: 31536000 (1 year)
    SECURE_HSTS_INCLUDE_SUBDOMAINS = False
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_PRELOAD = True