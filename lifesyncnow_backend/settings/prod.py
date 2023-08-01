from .common import *
import os
import dj_database_url
# from decouple import config
from dotenv import load_dotenv
load_dotenv()

DEBUG = True

# ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", default=['*']).split()

# DATABASES
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

# REDIS CELERY
from ..redis_celery.redis_celery_conf import *  # noqa
# email
from ..email.email_conf import *  # noqa
# ENVIRONMENT
# from ...env.env_prod_config import *  # noqa
env_file = os.path.join(BASE_DIR, 'env', '.env.dev')
load_dotenv(env_file)

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: True
}
