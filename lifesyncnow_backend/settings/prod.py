import os
# import dj_database_url
# from decouple import config
from dotenv import load_dotenv
from .common import *
load_dotenv()

DEBUG = False

SECRET_KEY = os.getenv['SECRET_KEY']

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS").split(" ")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('PROD_DB_NAME'),
        'USER': os.getenv('PROD_DB_USER'),
        'PASSWORD': os.getenv('PROD_DB_PASSWORD'),
        'HOST': "app-f50b6b84-f0cf-46fb-ae93-f8b96dde1e70-do-user-12706543-0.b.db.ondigitalocean.com",
        'PORT': "25060"
    }
}

REDIS_URL = os.environ['REDIS_URL']

CELERY_BROKER_URL = REDIS_URL


CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': REDIS_URL,
        'TIMEOUT': 10 * 60,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

# mailgun alternative email service for digitalocean
# EMAIL_HOST = os.environ['MAILGUN_SMTP_SERVER']
# EMAIL_HOST_USER = os.environ['MAILGUN_SMTP_LOGIN']
# EMAIL_HOST_PASSWORD = os.environ['MAILGUN_SMTP_PASSWORD']
# EMAIL_PORT = os.environ['MAILGUN_SMTP_PORT']

# email
from ..email.email_conf import *  # noqa
