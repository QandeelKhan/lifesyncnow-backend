from .common import *
import os
# import dj_database_url
# from decouple import config
from dotenv import load_dotenv
load_dotenv()

DEBUG = True

# ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", default=['*']).split()
ALLOWED_HOSTS = ["*"]

# DATABASES

# DATABASES = {
# 'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': os.getenv('PROD_DB_NAME'),
#        'USER': os.getenv('PROD_DB_USER'),
#        'PASSWORD': os.getenv('PROD_DB_PASSWORD'),
#        'HOST': "app-f50b6b84-f0cf-46fb-ae93-f8b96dde1e70-do-user-12706543-0.b.db.ondigitalocean.com",
#        'PORT': "25060"
#     }
#     'psql': {
#         # 'ENGINE': 'django.db.backends.postgresql',
#         # or
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'storefront2',
#         'HOST': 'localhost',
#         'USER': os.getenv('DEV_DB_USER'),
#         'PASSWORD': os.getenv('DEV_DB_PASSWORD')
#     },
#     'mysql': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'storefront2',
#         'HOST': 'localhost',
#         'USER': os.getenv('DEV_DB_USER'),
#         'PASSWORD': os.getenv('DEV_DB_PASSWORD')
#     },
# }


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.getenv('PROD_DB_NAME'),
#         'USER': os.getenv('PROD_DB_USER'),
#         'PASSWORD': os.getenv('PROD_DB_PASSWORD'),
#         'HOST': "app-f50b6b84-f0cf-46fb-ae93-f8b96dde1e70-do-user-12706543-0.b.db.ondigitalocean.com",
#         'PORT': "25060"
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ourblogdb',
        'HOST': 'localhost',
        'USER': 'ourbloguser',
        'PASSWORD': 'OurBlogPassword'
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


CELERY_BROKER_URL = 'redis://redis:6379/1'

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://redis:6379/2',
        'TIMEOUT': 10 * 60,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

# email
from ..email.email_conf import *  # noqa

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: True
}
