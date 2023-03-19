from django.db import models
from django.conf import settings
from django.utils import timezone
from .sbs_model import StepByStepGuid


class ContactUs(models.Model):
    step_by_step_guide = models.ManyToManyField(
        StepByStepGuid, related_name='contacts_us', blank=True)
    title = models.CharField(
        max_length=100, help_text="The title of the about page.")
    content = models.TextField(
        null=True, blank=True, help_text="The content of the about page.")
    paragraphs = models.ManyToManyField(
        'Paragraph', related_name='paragraphs')
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


class Paragraph(models.Model):
    """
    Model representing paragraphs within the contact us page.
    """
    contact_us = models.ForeignKey(
        'ContactUs', on_delete=models.CASCADE, related_name='contact_paragraphs', blank=True, null=True)
    paragraph_title = models.CharField(
        max_length=255, help_text='The title of the paragraph..', null=True, blank=True)
    paragraph_content = models.TextField(null=True, blank=True,
                                         help_text='The content of the paragraph..')
    order = models.PositiveIntegerField(default=0,
                                        help_text='The order in which the paragraph should appear in the contact us page..', blank=True, null=True)

    # class Meta:
    #     ordering = ['order']

    def __str__(self):
        return self.paragraph_title
