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

AWS_STORAGE_BUCKET_NAME = 'pruebaejemplo'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = 'AKIAJ7EJPWBZ2PNLUFBA'
AWS_SECRET_ACCESS_KEY = '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'

STATIC_URL = 'https://s3.amazonaws.com/cursoprodjango/'
MEDIA_URL = 'https://s3.amazonaws.com/cursoprodjango/'

MEDIA_ROOT = BASE_DIR.child('media')