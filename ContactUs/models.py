from django.db import models
from django.conf import settings
from django.utils import timezone
from .paragraph_with_sbs import Paragraph


class PrivacyPolicy(models.Model):
    title = models.CharField(
        max_length=100, help_text="The title of the about page.")
    content = models.TextField(
        null=True, blank=True, help_text="The content of the about page.")
    paragraphs_privacy_policy = models.ManyToManyField(
        'Paragraph', related_name='paragraphs_privacy_policy', blank=True)
    author_privacy_policy = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author_privacy_policy', help_text="The author of the contact us page.", null=True, blank=True)
    created_at = models.DateTimeField(
        default=timezone.now, help_text="The date and time when the contact us page was created.")
    updated_at = models.DateTimeField(
        auto_now=True, help_text="The date and time when the contact us post was last updated.")

    # Metadata
    class Meta:
        ordering = ("-created_at",)
        verbose_name_plural = "contact us"
        db_table = "PrivacyPolicy"

    def __str__(self):
        return self.title


class AdvertiseWithWellPlusGood(models.Model):
    title = models.CharField(
        max_length=100, help_text="The title of the about page.")
    content = models.TextField(
        null=True, blank=True, help_text="The content of the about page.")
    paragraphs_advertise_well_good = models.ManyToManyField(
        'Paragraph', related_name='paragraphs_advertise_well_good', blank=True)
    author_advertise_well_good = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='advertise_well_good', help_text="The author of the contact us page.")
    created_at = models.DateTimeField(
        default=timezone.now, help_text="The date and time when the contact us page was created.")
    updated_at = models.DateTimeField(
        auto_now=True, help_text="The date and time when the contact us post was last updated.")

    # Metadata
    class Meta:
        ordering = ("-created_at",)
        verbose_name_plural = "contact us"
        db_table = "Advertise-with-well-plus-good"

    def __str__(self):
        return self.title


class ContactUs(models.Model):
    title = models.CharField(
        max_length=100, help_text="The title of the about page.")
    content = models.TextField(
        null=True, blank=True, help_text="The content of the about page.")
    paragraphs = models.ManyToManyField(
        'Paragraph', related_name='paragraphs', blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='contact_us', help_text="The author of the contact us page.")
    created_at = models.DateTimeField(
        default=timezone.now, help_text="The date and time when the contact us page was created.")
    updated_at = models.DateTimeField(
        auto_now=True, help_text="The date and time when the contact us post was last updated.")

    # Metadata
    class Meta:
        ordering = ("-created_at",)
        verbose_name_plural = "contact us"
        db_table = "contact_us"

    def __str__(self):
        return self.title
