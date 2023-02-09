import os
from decouple import config
# from StrefrontBackend2.settings import BASE_DIR
from ..settings.common import BASE_DIR

# USE_SPACES = config('USE_SPACES', cast=bool, default=False)
USE_SPACES = False

if USE_SPACES:
    # settings
    AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
    AWS_DEFAULT_ACL = 'public-read'
    AWS_S3_ENDPOINT_URL = config('AWS_S3_ENDPOINT_URL')
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    # static settings
    AWS_LOCATION = 'space-django-boilerplate/static'
    STATIC_URL = f'https://shopingly-space.fra1.digitaloceanspaces.com/{AWS_LOCATION}/'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    # public media settings
    PUBLIC_MEDIA_LOCATION = 'space-django-boilerplate/media'
    MEDIA_URL = f'https://shopingly-space.fra1.digitaloceanspaces.com/{PUBLIC_MEDIA_LOCATION}/'

    DEFAULT_FILE_STORAGE = '<space-name>.cdn.backends.MediaRootS3Boto3Storage'
else:
    STATIC_URL = '/static/'
    STATIC_ROOT = BASE_DIR / "space-django-boilerplate/static"
    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR / 'space-django-boilerplate/media'

# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'space-django-boilerplate/static'),
# )
# helping material
# https://testdriven.io/blog/django-digitalocean-spaces/
# https://shopingly-space.fra1.digitaloceanspaces.com/media/productimg/0_98drx4MegZUq4iTd.jpeg
