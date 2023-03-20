from django.db import models
from django.conf import settings
from django.utils import timezone
from .paragraph_with_sbs import Paragraph


class ContactUs(models.Model):
    title = models.CharField(
        max_length=100, help_text="The title of the about page.")
    content = models.TextField(
        null=True, blank=True, help_text="The content of the about page.")
    paragraphs = models.ManyToManyField(
        'Paragraph', related_name='paragraphs', null=True, blank=True)
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
