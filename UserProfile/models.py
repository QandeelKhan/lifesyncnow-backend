from django.db import models
from django.conf import settings
from django.core.files.storage import default_storage
from decouple import config
from django.core.files.storage import FileSystemStorage
from PIL import Image

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


class UserProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name='user_profile')
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
