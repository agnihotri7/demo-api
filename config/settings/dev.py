import os 

from config.settings.base import *

DEBUG = True

ENABLE_API_ROOT = True

INSTALLED_APPS += [
    'django_extensions',
    # 'debug_toolbar',
]

# Django Debug Toolbar Allowd IPs
INTERNAL_IPS = (
    '127.0.0.1',
)

ALLOWED_HOSTS = ["*"]

MIDDLEWARE += [
    # add more middlewares
]

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    # '/var/www/static/',
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]
