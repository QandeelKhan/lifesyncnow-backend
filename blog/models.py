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
from django.utils import timezone
from .paragraph_with_sbs import BlogParagraph

# make custom storage backend for image
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


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.category_name)


class TopicType(models.Model):
    topic = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.topic)
# for more then one images and image_links we created BlogPostImage model


class BlogPostImage(models.Model):
    images = models.ImageField(upload_to='blog-images/',
                               storage=fs, validators=[validate_image], blank=True, null=True)
    # image_links = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return str(self.images)


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class BlogPost(models.Model):
    title = models.CharField(
        max_length=100, help_text="The title of the blog post.")
    content = models.TextField(
        null=True, blank=True, help_text="The title of the blog post.")
    status = models.IntegerField(
        choices=STATUS, default=0, null=True, blank=True)

    slug = models.SlugField(
        max_length=255,
        unique=True,
        null=True,
        blank=True,
        help_text="A URL-friendly version of the blog post's title.",
    )
    cover_image = models.ImageField(upload_to='blog-images/',
                                    storage=fs, validators=[validate_image], null=True, blank=True)
    paragraphs = models.ManyToManyField(
        BlogParagraph, related_name='paragraphs')
    # initial_paragraph = models.TextField()
    # paragraph_heading = models.CharField(max_length=255)
    quote = models.CharField(max_length=255, null=True, blank=True)
    quote_writer = models.CharField(max_length=255, null=True, blank=True)
    # second_paragraph = models.TextField()
    post_images = models.ManyToManyField(
        BlogPostImage, related_name='post_images', blank=True)
    # paragraph_after_image = models.TextField(null=True, blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts', help_text="The author of the blog post.")
    # created_at = models.DateTimeField(auto_now_add=True)

    created_at = models.DateTimeField(
        default=timezone.now, help_text="The date and time when the blog post was created.")
    updated_at = models.DateTimeField(
        auto_now=True, help_text="The date and time when the blog post was last updated.")
    most_recent_posts = models.BooleanField(
        default=False, null=True, blank=True)
    featured_posts = models.BooleanField(default=False, null=True, blank=True)
    older_posts = models.BooleanField(default=False, null=True, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="post_category")
    topic_type = models.ForeignKey(
        TopicType, on_delete=models.CASCADE, related_name="post_topic", null=True, blank=True)

    # Metadata
    class Meta:
        ordering = ("-created_at",)
        verbose_name_plural = "blog posts"
        db_table = "blog_posts"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Returns the absolute URL of the blog post.
        """
        return reverse("blog:post_detail", kwargs={"slug": self.slug})

    def is_recent(self):
        """
        Returns True if the blog post was created within the last 30 days.
        """
        delta = timezone.now() - self.created_at
        return delta.days <= 30

    def is_older(self):
        """
        Returns True if the blog post was created more than 30 days ago.
        """
        delta = timezone.now() - self.created_at
        return delta.days > 30

    def save(self, *args, **kwargs):
        """
        Override the save method to set the `most_recent_posts` and `older_posts`
        fields based on `is_recent` and `is_older` methods respectively.
        """
        self.most_recent_posts = self.is_recent()
        self.older_posts = self.is_older()
        #
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


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
