
## config/settings.py


```python
# Settings for smtp
EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_PORT = os.environ.get("EMAIL_PORT")

if EMAIL_PORT is not None:
    EMAIL_PORT = int(EMAIL_PORT)

if PRODUCTION and not DEBUG:
    EMAIL_USE_TLS = True
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
else:
    EMAIL_USE_TLS = False
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
```

## .env

```
# Email smtp backend
EMAIL_HOST=host
EMAIL_HOST_USER=host-user
EMAIL_HOST_PASSWORD=host-pass
EMAIL_PORT=port
```

