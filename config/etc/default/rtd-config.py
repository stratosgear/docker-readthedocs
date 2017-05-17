from readthedocs.settings.dev import *

import os
environ = os.environ

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': environ['DB_NAME'],
        'USER': environ['DB_USER'],
        'PASSWORD': environ['DB_PASS'],
        'HOST': 'rtd-db',
        'PORT': 5432,
    }
}
SITE_ROOT = '/app'
ES_HOSTS = ['rtd-elk:9200']
REDIS = {
    'host': 'rtd-redis',
    'port': 6379,
    'db': 0
}
BROKER_URL = 'redis://rtd-redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://rtd-redis:6379/0'
DEBUG = True
CELERY_ALWAYS_EAGER = False
