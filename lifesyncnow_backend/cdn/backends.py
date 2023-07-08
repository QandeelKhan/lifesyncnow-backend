from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

# making settings for our static assets to after that set in conf.py
# this will make upload our static folder into digitalocean,


class StaticStorage(S3Boto3Storage):
    bucket_name = 'life-sync-now-bucket'
    location = 'space-lifesyncnow/static'
    # just for aws not for the digitalocean


class MediaStorage(S3Boto3Storage):
    bucket_name = 'life-sync-now-bucket'
    location = 'space-lifesyncnow/media'
    # default_acl = None
    # file_overwrite = False


# above provided locations we set similar to our local settings so the directories
# name and locations on the our hosted app on cloud look similar to our local file
# structure. we can type any name i.e "static-abc", "root-abcd".
