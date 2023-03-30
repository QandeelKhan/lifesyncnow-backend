from django.db import models
from django.core.files.storage import default_storage
from decouple import config
from django.core.files.storage import FileSystemStorage
from PIL import Image

# Create your models here.
USE_SPACES = config('USE_SPACES', cast=bool, default=False)
if USE_SPACES:
    fs = default_storage
else:
    fs = FileSystemStorage(location='space-our-blog-backend/media')


def validate_image(image):
    try:
        img = Image.open(image)
        img.verify()
    except (IOError, SyntaxError) as e:
        raise ValidationError("Invalid image: %s" % e)


class FollowUs(models.Model):
    facebook_link = models.URLField(max_length=255, null=True, blank=True)
    twitter_link = models.URLField(max_length=255, null=True, blank=True)
    instagram_link = models.URLField(max_length=255, null=True, blank=True)
    youtube_link = models.URLField(max_length=255, null=True, blank=True)
    pinterest_link = models.URLField(max_length=255, null=True, blank=True)


class PageTemplate(models.Model):
    logo_name = models.CharField(max_length=255, null=True, blank=True)
    logo_description = models.CharField(max_length=255, null=True, blank=True)
    logo_image = models.ImageField(upload_to='template-images/',
                                   storage=fs, validators=[validate_image], null=True, blank=True)
    copyright = models.CharField(max_length=255, null=True, blank=True)
    follow_us = models.ForeignKey(
        FollowUs, on_delete=models.CASCADE, related_name='follow_us_page_template', null=True, blank=True)
