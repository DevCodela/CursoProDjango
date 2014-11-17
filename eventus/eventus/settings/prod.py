from .base import *

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'eventusdbprod',
        'USER': 'eventususerprod',
        'PASSWORD': 'eventus',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

INSTALLED_APPS = INSTALLED_APPS + (
		'storages',
	)	

AWS_STORAGE_BUCKET_NAME = 'cursoprodjango'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = 'AKIAIZ2L6GXFNKJYHJMQ'
AWS_SECRET_ACCESS_KEY = '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'

STATIC_URL = 'https://s3.amazonaws.com/cursoprodjango/'
MEDIA_URL = 'https://s3.amazonaws.com/cursoprodjango/'

MEDIA_ROOT = BASE_DIR.child('media')