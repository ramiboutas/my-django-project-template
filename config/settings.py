from pathlib import Path
import dotenv
import sys
import os


# Setup

# Build paths inside the project like this: BASE_DIR / "subdir".
BASE_DIR = Path(__file__).resolve().parent.parent

# Production 
PRODUCTION = str(os.environ.get('PRODUCTION')) == '1'

# Use Postgres (otherwise Sqlite)
USE_POSTGRES = str(os.environ.get('USE_POSTGRES')) == '1'

# Load env vars from .env file if not testing
try:
    command = sys.argv[1]
except IndexError:
    command = "help"

if command != "test":
    dotenv.load_dotenv(dotenv_path=BASE_DIR / ".env")


# Django Core and Contrib Settings

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don"t run with debug turned on in production!
DEBUG = str(os.environ.get('DEBUG')) == '1'

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    # My apps

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
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

if USE_POSTGRES:
    POSTGRES_DB = os.environ.get('POSTGRES_DB')
    POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
    POSTGRES_USER = os.environ.get('POSTGRES_USER')
    POSTGRES_HOST = os.environ.get('POSTGRES_HOST')
    POSTGRES_PORT = os.environ.get('POSTGRES_PORT')
    POSTGRES_TESTS_DB = os.environ.get('POSTGRES_TESTS_DB')

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': POSTGRES_DB,
            'USER': POSTGRES_USER,
            'PASSWORD': POSTGRES_PASSWORD,
            'HOST': POSTGRES_HOST,
            'PORT': POSTGRES_PORT,
            'TEST': {
             'NAME': 'test_db',
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
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-UK"

TIME_ZONE = "Europe/Berlin"

USE_I18N = True

USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# The name of the class to use for starting the test suite.

TEST_RUNNER = "config.test.TestRunner"


# Project Settings

# Storage
USE_SPACES = os.environ.get("USE_SPACES") == "1"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static_dev"),
]

if USE_SPACES:

    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

    AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
    AWS_S3_ENDPOINT_URL = "https://fra1.digitaloceanspaces.com"
    AWS_S3_CUSTOM_DOMAIN = "spaces.ramiboutas.com"
    AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400", "ACL": "public-read"}
    # AWS_LOCATION = f"https://{AWS_STORAGE_BUCKET_NAME}.fra1.digitaloceanspaces.com"

    AWS_DEFAULT_ACL = "public-read"
    AWS_S3_SIGNATURE_VERSION = "s3v4"

    DEFAULT_FILE_STORAGE = "config.storage_backends.MediaRootStorage"
    STATICFILES_STORAGE = "config.storage_backends.StaticRootStorage"

    AWS_STATIC_LOCATION = os.environ.get("AWS_STATIC_LOCATION")
    # STATIC_URL = f"https://{AWS_S3_ENDPOINT_URL}/{AWS_STATIC_LOCATION}/"
    STATIC_URL = "https://{}/{}/".format(AWS_S3_CUSTOM_DOMAIN, AWS_STATIC_LOCATION)
    STATIC_ROOT = f"{AWS_STATIC_LOCATION}/"

    AWS_MEDIA_LOCATION = "englishstuff-media"
    AWS_MEDIA_DEFAULT_ACL = "public-read"
    # MEDIA_URL = f"https://{AWS_STORAGE_BUCKET_NAME}.fra1.digitaloceanspaces.com/{AWS_MEDIA_LOCATION}/" # it worked
    # MEDIA_URL = f"https://{AWS_S3_ENDPOINT_URL}/{AWS_MEDIA_LOCATION}/"
    MEDIA_URL = "{}/{}/".format(AWS_S3_CUSTOM_DOMAIN, AWS_MEDIA_LOCATION)
    MEDIA_ROOT = f"{AWS_MEDIA_LOCATION}/"

else:
    STATIC_URL = "/static/"
    STATIC_ROOT = os.path.join(BASE_DIR, "static")
    MEDIA_URL = "/media/"
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")


# https://stackoverflow.com/questions/35760943/how-can-i-enable-cors-on-django-rest-framework
# CORS_ORIGIN_ALLOW_ALL = True
# CORS_ALLOW_CREDENTIALS = True
# CORS_ALLOW_HEADERS = "access-control-allow-origin"


if PRODUCTION:
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_HSTS_SECONDS = 31_536_000 #31536000 # usual: 31536000 (1 year)
    SECURE_HSTS_INCLUDE_SUBDOMAINS = False
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_PRELOAD = True
    PREPEND_WWW = True

    # caching
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.redis.RedisCache",
            "LOCATION": "redis://127.0.0.1:6379",
        }
    }
