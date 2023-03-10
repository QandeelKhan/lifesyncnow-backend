from django.db import models
# from UserManagement.models import User
from django.core.files.storage import FileSystemStorage
from PIL import Image
# to make blog independent from User but getting
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.core.files.storage import default_storage
from decouple import config


# make custom storage backend for image
USE_SPACES = config('USE_SPACES', cast=bool, default=True)
if USE_SPACES:
    fs = default_storage
else:
    fs = FileSystemStorage(location='space-our-resume/media')


def validate_image(image):
    try:
        img = Image.open(image)
        img.verify()
    except (IOError, SyntaxError) as e:
        raise ValidationError("Invalid image: %s" % e)


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.category_name)
# for more then one images and image_links we created BlogPostImage model


class BlogPostImage(models.Model):
    images = models.ImageField(upload_to='blog-images/',
                               storage=fs, validators=[validate_image], blank=True, null=True)
    # image_links = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return str(self.images)


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='blog-images/',
                                    storage=fs, validators=[validate_image])
    initial_paragraph = models.TextField()
    paragraph_heading = models.CharField(max_length=255)
    quote = models.CharField(max_length=255)
    quote_writer = models.CharField(max_length=255)
    second_paragraph = models.TextField()
    post_images = models.ManyToManyField(
        BlogPostImage, related_name='post_images')
    paragraph_after_image = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="post_category")

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        BlogPost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comment_text = models.TextField()

    def __str__(self):
        return self.comment_text

    def __str__(self):
        return f'{self.author.first_name} {self.author.last_name}: {self.comment_text}'


class Reply(models.Model):
    comment_id = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name='replies')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reply_text = models.TextField()

    def __str__(self):
        return self.reply_text

    def __str__(self):
        return f'{self.author.first_name} {self.author.last_name}: {self.reply_text}'
