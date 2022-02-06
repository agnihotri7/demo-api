from config.settings.base import *

DEBUG = False

ENABLE_API_ROOT = False

ALLOWED_HOSTS = []

CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = True

SESSION_COOKIE_HTTPONLY = True

INSTALLED_APPS += [
]

# Setting for X-Forwarded-Proto proxy and host
USE_X_FORWARDED_HOST  = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
