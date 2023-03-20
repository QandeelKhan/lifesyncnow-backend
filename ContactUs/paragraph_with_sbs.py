from django.db import models


class StepByStepGuide(models.Model):
    """
    A model representing a step-by-step guide within a blog post.
    """
    # Fields
    contact_us = models.ForeignKey(
        'ContactUs',
        on_delete=models.CASCADE,
        related_name='step_by_step_guides_contact_specific',
        help_text='The blog post that this step-by-step guide belongs to.'
    )
    blog_paragraphs = models.ForeignKey(
        'Paragraph',
        on_delete=models.CASCADE,
        related_name='blog_paragraphs',
        help_text='The blog post that this step-by-step guide belongs to.',
        null=True, blank=True
    )
    sbs_guide_number = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        help_text='Number of the step-by-step guides on a post. Can be used for multiple purposes.'
    )

    sub_heading = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text='The text of this subheading.'
    )
    sub_content = models.TextField(
        null=True,
        blank=True,
        help_text='The text of this subcontent.'
    )
    # Metadata
    sbs_index = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        help_text='The number of this subsection within the parent step-by-step guide.'
    )
    sbs_self_refer = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='sbsguides',
        on_delete=models.CASCADE,
        help_text='The parent subsection that this subsection belongs to.'
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'step-by-step guide'
        verbose_name_plural = 'step-by-step guides'
        db_table = 'step_by_step_guides_contact_us_specific'


class Paragraph(models.Model):
    """
    Model representing a clause within the terms and conditions.
    """
    contact_us = models.ForeignKey(
        'ContactUs', on_delete=models.CASCADE, related_name='contact_paragraphs', blank=True, null=True)
    paragraph_title = models.CharField(
        max_length=255, help_text='The title of the clause..', null=True, blank=True)
    paragraph_content = models.TextField(null=True, blank=True,
                                         help_text='The content of the clause..')
    step_by_step_guide = models.ManyToManyField(
        'StepByStepGuide', related_name='posts_sbs', blank=True)
    order = models.PositiveIntegerField(default=0,
                                        help_text='The order in which the clause should appear in the terms and conditions..', blank=True, null=True)

    def __str__(self):
        return self.paragraph_title

    # Metadata
    # class Meta:
    #     ordering = ['id']
    #     verbose_name = 'Paragraph'
    #     verbose_name_plural = 'BlogParagraphs'
    #     db_table = 'BlogParagraphs'
