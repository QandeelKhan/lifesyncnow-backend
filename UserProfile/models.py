from django.db import models
from django.conf import settings
from django.core.files.storage import default_storage
from decouple import config
from django.core.files.storage import FileSystemStorage
from PIL import Image
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

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


class Role(models.Model):
    role_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.role_name)


User = get_user_model()


class UserProfile(models.Model):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name='user_profile')
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
        null=True,
        blank=True,
    )
    user_slug = models.SlugField(
        max_length=255,
        unique=True,
        null=True,
        blank=True,
        help_text="A URL-friendly version of the blog post's title.",
    )
    bio = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile-images/',
                                      storage=fs, validators=[validate_image], null=True, blank=True)
    role = models.ForeignKey(
        Role, on_delete=models.CASCADE, related_name="user_role")
    country = models.CharField(max_length=150, null=True, blank=True)
    city = models.CharField(max_length=150, null=True, blank=True)
    twitter_acc = models.CharField(max_length=300, null=True, blank=True)
    facebook_acc = models.CharField(max_length=300, null=True, blank=True)
    instagram_acc = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}'s Profile"

    def related_posts(self):
        """
        Returns all the blog posts related to the user of this profile.
        """
        return self.user.blog_posts.all()


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        # User instance is newly created
        UserProfile.objects.create(user=instance,
                                   first_name=instance.first_name,
                                   last_name=instance.last_name,
                                   email=instance.email,
                                   user_slug=instance.user_slug,
                                   ),
    else:
        # User instance is being updated
        user_profile, created = UserProfile.objects.get_or_create(
            user=instance)
        user_profile.first_name = instance.first_name
        user_profile.last_name = instance.last_name
        user_profile.email = instance.email
        user_profile.profile_image = instance.profile_image
        user_profile.user_slug = instance.user_slug
        user_profile.save()
