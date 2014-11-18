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
AWS_ACCESS_KEY_ID = 'AKIAJ3J5C2UG3C2H6OYQ'
AWS_SECRET_ACCESS_KEY = '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'

STATIC_URL = 'https://s3.amazonaws.com/cursoprodjango/'
MEDIA_URL = 'https://s3.amazonaws.com/cursoprodjango/'

MEDIA_ROOT = BASE_DIR.child('media')