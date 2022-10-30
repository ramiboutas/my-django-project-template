
# Using Storages


## requirements.in

```
django-storages
boto3
```


## config/storage_backends.py

```python

from __future__ import annotations

from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticRootStorage(S3Boto3Storage):
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    location = settings.AWS_STATIC_LOCATION
    default_acl = "public-read"


class MediaRootStorage(S3Boto3Storage):
    bucket_name = settings.AWS_STORAGE_BUCKET_NAME
    location = settings.AWS_MEDIA_LOCATION
    default_acl = settings.AWS_MEDIA_DEFAULT_ACL

```

## config/settings.py


```python
# Storage
USE_DO_SPACES = str(os.environ.get("USE_DO_SPACES")) == "1"

if USE_DO_SPACES:

    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

    AWS_DEFAULT_ACL = "public-read"
    AWS_S3_SIGNATURE_VERSION = "s3v4"

    AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME")
    AWS_S3_ENDPOINT_URL = "https://fra1.digitaloceanspaces.com"
    AWS_S3_CUSTOM_DOMAIN = "spaces.ramiboutas.com"
    AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400", "ACL": AWS_DEFAULT_ACL}

    DEFAULT_FILE_STORAGE = "config.storage_backends.MediaRootStorage"
    STATICFILES_STORAGE = "config.storage_backends.StaticRootStorage"

    AWS_STATIC_LOCATION = "my-static-folder"
    STATIC_URL = "https://{}/{}/".format(AWS_S3_CUSTOM_DOMAIN, AWS_STATIC_LOCATION)
    STATIC_ROOT = f"{AWS_STATIC_LOCATION}/"

    AWS_MEDIA_LOCATION = "my-media-folder"
    AWS_MEDIA_DEFAULT_ACL = "public-read"
    MEDIA_URL = "{}/{}/".format(AWS_S3_CUSTOM_DOMAIN, AWS_MEDIA_LOCATION)
    MEDIA_ROOT = f"{AWS_MEDIA_LOCATION}/"


```


## .env

```

# Digital Ocean Spaces
# set USE_SPACES to 1 if I want to store static & media files on Digital Ocean Spaces Service
USE_DO_SPACES=0
AWS_ACCESS_KEY_ID=access-key-id
AWS_SECRET_ACCESS_KEY=secret-access-key
AWS_STORAGE_BUCKET_NAME=bucket-name


```
