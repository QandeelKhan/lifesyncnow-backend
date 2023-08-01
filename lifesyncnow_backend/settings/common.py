from decouple import config
from datetime import timedelta
import os
from pathlib import Path
from pprint import pprint
# from celery.schedules import crontab
from dotenv import load_dotenv
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

env_file = os.path.join(BASE_DIR, 'env', '.env.dev')
load_dotenv(env_file)
SECRET_KEY = os.getenv('SECRET_KEY')

# --------APPS STRUCTURE----------#
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'channels',
]

PROJECT_APPS = [
    'blog',
    'legal',
    'meta',
    'global_content',
    'page',
    'subscriber',
    'user_management',
    'user_profile',
    'lifesyncnow_backend',
    # 'playground',
    # 'store',
    # 'core',
    # 'tags',
    # 'like',
    # --USER MANAGEMENT,
    # 'allauth',
    # 'allauth.account',
    # 'allauth.socialaccount',
    # 'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.twitter',
    #
    # 'rest_auth',
    # 'rest_auth.registration',
    # 'rest_framework.authtoken',
]

THIRD_PARTY_APPS = [
    'django_filters',
    'corsheaders',
    'rest_framework',
    'djoser',
    'silk',
    'debug_toolbar',
    'rest_framework_swagger',
    'dbbackup',
    'rest_framework_simplejwt',
    'ckeditor',
    'ckeditor_uploader',
    'defender',
]

# SERVER_URL = 'http://127.0.0.1:8000'
SERVER_URL = '127.0.0.1'
INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS
# --------APPS STRUCTURE----------#

# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'channels.layers.InMemoryChannelLayer',
#     },
# }
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("redis", 6379)],
        },
    },
}


# Backup settings
DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': BASE_DIR / 'DjangoBackup'}
DBBACKUP_CLEANUP_KEEP = 3  # number of backups to keep
DBBACKUP_EXTENSION = 'backup'
DBBACKUP_CLEANUP_EXTENSION = 'backup'
# Restore settings
DBBACKUP_RESTORE_OPTIONS = ['--noinput']
DBBACKUP_RESTORE_DB = 'default'

# ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_UNIQUE_EMAIL = True

# LOGIN_REDIRECT_URL = '/user_management(app name)/profile(url name)/'

# GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
# GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
# TWITTER_CONSUMER_KEY = os.getenv("TWITTER_CONSUMER_KEY")
# TWITTER_CONSUMER_SECRET = os.getenv("TWITTER_CONSUMER_SECRET")

# SOCIALACCOUNT_PROVIDERS = {
#     'google': {
#         'APP_ID': GOOGLE_CLIENT_ID,
#         'APP_SECRET': GOOGLE_CLIENT_SECRET,
#         'SCOPE': ['profile', 'email'],
#         'AUTH_PARAMS': {
#             'access_type': 'online',
#         }
#     },
#     'twitter': {
#         'KEY': TWITTER_CONSUMER_KEY,
#         'SECRET': TWITTER_CONSUMER_SECRET,
#     },
# }

# from ..google.settings_secret import *  # noqa

AUTHENTICATION_BACKENDS = [
    # ...
    'django.contrib.auth.backends.ModelBackend',
    # 'allauth.account.auth_backends.AuthenticationBackend',
]


MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    # 'silk.middleware.SilkyMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'defender.middleware.FailedLoginMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# if settings.DEBUG:
#     MIDDLEWARE += ['silk.middleware.SilkyMiddleware']

INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]

ROOT_URLCONF = 'lifesyncnow_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'lifesyncnow_backend.wsgi.application'
ASGI_APPLICATION = 'lifesyncnow_backend.asgi.application'

# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
from ..cdn.storage_conf import *  # noqa

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'COERCE_DECIMAL_TO_STRING': False,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

AUTH_USER_MODEL = 'user_management.User'


DJOSER = {
    'SERIALIZERS': {
        'user_create': 'user_management.serializers.UserCreateSerializer',
        'current_user': 'user_management.serializers.UserSerializer',
    }
}

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('JWT',),
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1)
}

DEFAULT_FROM_EMAIL = 'from@haiderbuy.com'

ADMINS = [
    ('Haider', 'admin@haiderbuy.com')
]

# CELERY_BEAT_SCHEDULE = {
#     'notify_customers': {
#         'task': 'playground.tasks.notify_customers',
#         'schedule': 5,
#         'args': ['Hi World'],
#     }
# }

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler'
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'general.log',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        '': {
            'handlers': ['console', 'file'],
            'level': os.environ.get('DJANGO_LOG_LEVEL', 'INFO')
        },
    },
    'formatters': {
        'verbose': {
            'format': '{asctime} ({levelname}) - {name} - {message}',
            'style': '{'
        }
    }
}

# -----SIMPLEJWT
SIMPLE_JWT = {
    # 'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'ACCESS_TOKEN_LIFETIME': timedelta(seconds=20),
    'REFRESH_TOKEN_LIFETIME': timedelta(hours=24),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',
}

PASSWORD_RESET_TIMEOUT = 900  # 900 Sec = 15min

# for react origin
SECURE_CONTENT_TYPE_NOSNIFF = False
SECURE_BROWSER_XSS_FILTER = False
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
X_FRAME_OPTIONS = 'DENY'

# -----CORS

# For development purposes.
# but in django 4
# CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
# ALLOWED_HOSTS = ["https://lifesyncnow.com", "https://www.lifesyncnow.com", "http://0.0.0.0:8000",
#                  "http://localhost:8000", "localhost:8000", 'localhost', "http://localhost:3000", "http://127.0.0.1", "127.0.0.1", "0.0.0.0", "http://0.0.0.0", "http://0.0.0.0:8000", "https://life-sync-now-bucket.s3.amazonaws.com", "http://lifesyncnow-backend:8000", "http://lifesyncnow-backend", "lifesyncnow-backend"]
ALLOWED_HOSTS = ["*"]
PASSWORD_RESET_TIMEOUT = 900  # 900 Sec = 15min
# For development purposes.

# we whitelist localhost:3000 because that's where frontend will be served
# CORS_ORIGIN_WHITELIST = ['*']
CORS_ORIGIN_WHITELIST = ["https://lifesyncnow.com", "https://www.lifesyncnow.com", "http://0.0.0.0:8000",
                         "http://localhost:8000", "http://localhost:3000", "https://life-sync-now-bucket.s3.amazonaws.com", "http://lifesyncnow-backend:8000", "http://lifesyncnow-backend"]
CORS_ORIGIN_ALLOW_ALL = True

# for react origin
# SECURE_CONTENT_TYPE_NOSNIFF = False
# SECURE_BROWSER_XSS_FILTER = False
# SECURE_SSL_REDIRECT = False
# SESSION_COOKIE_SECURE = False
# CSRF_COOKIE_SECURE = False
# X_FRAME_OPTIONS = 'DENY'
# CSRF_TRUSTED_ORIGINS = ["*"]
CORS_ALLOWED_METHODS = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'OPTIONS']
CSRF_TRUSTED_ORIGINS = ["https://lifesyncnow.com", "https://www.lifesyncnow.com", "http://0.0.0.0:8000",
                        "http://localhost:8000", "http://localhost:3000", "http://localhost:8000", "http://localhost:3000", "http://0.0.0.0:8000", "http://lifesyncnow-backend:8000", "http://lifesyncnow-backend"]
# As of Django 4.0, the values in the CSRF_TRUSTED_ORIGINS setting must start with a scheme (usually http:// or https://)

# NOTE: django-ckeditor will not work with S3 through django-storages without this line in settings.py:
# CKEDITOR_THUMBNAIL_SIZE = (300, 300)
# CKEDITOR_IMAGE_QUALITY = 40
# below line stoping me from sending image to server and giving 500 error
# CKEDITOR_FILENAME_GENERATOR = 'utils.get_filename'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'custom',
        'toolbar_custom': [
            ['Format', 'Styles', 'Bold', 'Italic',
                'Underline', 'Strike'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Image', 'Table', 'Link', 'HorizontalRule', 'SpecialChar'],
            ['Cut', 'Copy', 'Paste', 'PasteText',
                'PasteFromWord', '-', 'Undo', 'Redo'],
            ['Source', 'CodeSnippet', 'Find', 'Form', 'Iframe',]
        ],
        'extraAllowedContent': ['iframe[*]',],
        'filebrowserUploadUrl': '/ckeditor/upload/',
        # autoembed: this autoembed plugin will automatically make a url/link to behave as an embed link.
        # autolink: A simple plugin that turns the pasted or typed URL text into a link. For example, "http://example.com" will become "<a href=“http://example.com”>http://example.com</a>".
        # forms/Form (extension-name/interface name): To add forms like interface in content
        # iframe(Iframe): (in my case in filtered content it did not shows some iframes for security reason on my react.only works when giving user a button like think where he can click i.e "see now" and it shows a popup msg to enable js in browser, as by default js is off in browser) This plugin provides the dialog to insert and edit inline frames (<iframe> elements) into the editor content. This plugin needs to be distinguished from the IFrame Dialog Field plugin which lets you embed another HTML page in the dialog for interaction.
        # image2(Image): enhance the default Image interface by allowing things like make image center as well.
        'extraPlugins': ['codesnippet', 'autoembed', 'autolink', 'find', 'forms', 'iframe', 'image']
        # 'headingcenter_headingLevels': 'h1:h6',
        # 'custom_content': {
        #     'js': ['ckeditor/custom_config.js'], }
    },
}

# CKEDITOR_CONFIGS = {
#     'default': {
#         'toolbar': 'full',
#         'height': 300,
#         'width': 300,
#     },
#     'content': {
#         'toolbar': 'Custom',
#         'toolbar_Custom': [
#             ['Bold', 'Italic', 'Underline'],
#             ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-',
#                 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
#             ['Link', 'Unlink'],
#             ['RemoveFormat', 'Source']
#         ]
#     },
#     'awesome_ckeditor': {
#         'toolbar': 'Basic',
#     },
#     'custom_content': {
#         'js': ['./space-licesyncnow/static/ckeditor/custom_config.js'],
#     },
# }
# CKEDITOR_CONFIGS = {
#     'content': {
#         'toolbar': 'full',
#         'height': 300,
#         'width': 300,
#     },
# }
# CKEDITOR_CONFIGS = {
#     'default': {
#         'toolbar': 'Custom',
#         'toolbar_Custom': [
#             ['Bold', 'Italic', 'Underline'],
#             ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-',
#                 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
#             ['Link', 'Unlink'],
#             ['RemoveFormat', 'Source']
#         ]
#     }
# }


# -------Defender settings (sometimes required to restart for changes to take effect)
DEFENDER_LOGIN_FAILURE_LIMIT = 5  # (default is 3)
DEFENDER_COOLOFF_TIME = 60  # (default 300(5,mints))
DEFENDER_USERNAME_FORM_FIELD = 'email'
DEFENDER_LOCKOUT_TEMPLATE = 'blocked.html'

# -------CAPTCHA SETTINGS
RECAPTCHA_SITE_KEY = os.getenv('RECAPTCHA_SITE_KEY')
RECAPTCHA_SECRET_KEY = os.getenv('RECAPTCHA_SECRET_KEY')
