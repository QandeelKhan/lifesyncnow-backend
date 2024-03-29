from .common import *
import os
import dj_database_url
# from decouple import config
from dotenv import load_dotenv
load_dotenv()

DEBUG = True

# ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", default=['*']).split()

# DATABASES

# DATABASES = {
# 'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
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
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'LifeSyncNowDB',
#         'HOST': 'localhost',
#         'HOST': "app-f50b6b84-f0cf-46fb-ae93-f8b96dde1e70-do-user-12706543-0.b.db.ondigitalocean.com",
#         'USER': 'lifesyncnow-user',
#         'PASSWORD': 'LifeSyncNowPassword'
#     },
# }

# with docker
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        # in development we can use name as * to connect with any name but in production we have to write the actual hostname of our db
        # 'HOST': "*",
        'HOST': 'db1',
        'PORT': 5432,
    }
}


# # REDIS CELERY
# from ..redis_celery.redis_celery_conf import *  # noqa

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        # setting redis database number as 0
        'LOCATION': 'redis://redis:6379/0',
        # 'TIMEOUT': 10 * 60,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

CELERYD_LOG_LEVEL = 'CELERY-INFO'
CELERY_APP = 'lifesyncnow_backend.celery_app'
DEFENDER_CACHE = 'default'
BROKER_URL = 'redis://redis:6379/0'
REDIS_URL = 'redis://redis:6379/0'
CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
CELERY_CACHE_BACKEND = 'default'
CELERY_BACKEND_URL = 'redis://redis:6379/0'
CELERY_FLOWER_PORT = 5555
DEFENDER_REDIS_URL = "redis://redis:6379/1"

# EMAIL
from ..email.email_conf import *  # noqa
# from ...env.env_dev_config import *  # noqa
env_file = os.path.join(BASE_DIR, 'env', '.env.dev')
load_dotenv(env_file)


DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: True
}
