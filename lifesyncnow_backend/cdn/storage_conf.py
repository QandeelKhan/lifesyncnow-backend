import os
from decouple import config
# from StrefrontBackend2.settings import BASE_DIR
from ..settings.common import BASE_DIR
from django.conf import settings

# USE_SPACES = config('USE_SPACES', cast=bool, default=False)
USE_SPACES = False

if USE_SPACES:
    # settings
    # AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
    AWS_ACCESS_KEY_ID = "AKIA5NZV4M7USLYGOXPP"
    AWS_SECRET_ACCESS_KEY = "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"
    AWS_STORAGE_BUCKET_NAME = "life-sync-now-bucket"
    AWS_S3_REGION_NAME = "ap-south-1"
    AWS_DEFAULT_ACL = None
    #
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static files settings
    # STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/space-lifesyncnow/static/'
    STATICFILES_STORAGE = 'lifesyncnow_backend.cdn.backends.StaticStorage'

    # Media files settings
    PUBLIC_MEDIA_LOCATION = 'space-lifesyncnow/media'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{PUBLIC_MEDIA_LOCATION}/'
    DEFAULT_FILE_STORAGE = 'lifesyncnow_backend.cdn.backends.MediaStorage'
    #
    # Static files settings
    # STATIC_URL = "https://life-sync-now-bucket.s3.ap-south-1.amazonaws.com/space-lifesyncnow/static/"
    #
    # s3 static settings
    AWS_LOCATION = 'space-lifesyncnow/static'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/'
    # STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage
    #
    # CKEDITOR_UPLOAD_PATH = "uploads/"
if not USE_SPACES:
    # PUBLIC_MEDIA_LOCATION = 'space-lifesyncnow/media'
    # ckeditor related only
    # AWS_QUERYSTRING_AUTH = False
    # CKEDITOR_FORCE_JPEG_COMPRESSION = True
    # CKEDITOR_IMAGE_BACKEND = "pillow"
    # CKEDITOR_IMAGE_BACKEND = "ckeditor_uploader.backends.PillowBackend"
    # CKEDITOR_BROWSE_SHOW_DIRS = True
    # CKEDITOR_ALLOW_NONIMAGE_FILES = True
    # ckeditor related only
    CKEDITOR_UPLOAD_PATH = 'uploads/'
    CKEDITOR_IMAGE_BACKEND = 'pillow'
    CKEDITOR_UPLOAD_SLUGIFY_FILENAME = False
    CKEDITOR_ALLOW_NONIMAGE_FILES = False  # Adjust as needed
    CKEDITOR_RESTRICT_BY_USER = True  # If you want to restrict by user

    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'space-lifesyncnow/static')
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'space-lifesyncnow/media')
    CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
    CKEDITOR_UPLOAD_PATH = f'uploads/'
    # CKEDITOR_UPLOAD_PATH = f'localhost:8000{MEDIA_URL}uploads/'
    "http://localhost:8000/media/space-lifesyncnow/media/commerce_season.jpeg"

    print(CKEDITOR_UPLOAD_PATH)
    print(CKEDITOR_UPLOAD_PATH)
    print(CKEDITOR_UPLOAD_PATH)

# helping material
# https://testdriven.io/blog/django-digitalocean-spaces/
# https://shopingly-space.fra1.digitaloceanspaces.com/media/productimg/0_98drx4MegZUq4iTd.jpeg
