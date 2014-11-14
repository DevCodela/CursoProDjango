from .base import *

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd3fei0gl3p80ni',
        'USER': 'ineekdzsibwbij',
        'PASSWORD': 'A8Hgrag8Wb5NBou_IgHJl6RiyF',
        'HOST': 'ec2-54-204-39-187.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')