from django.db import models


class StepByStepGuid(models.Model):
    """
    A model representing a step-by-step guide within a contact us page.
    """
    # Fields
    blog_post = models.ForeignKey(
        'ContactUs',
        on_delete=models.CASCADE,
        related_name='step_by_step_guides_contact',
        help_text='The contact us page that this step-by-step guide belongs to.'
    )
    sbs_guide_number = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        help_text='Number of the step-by-step guides on a post. Can be used for multiple purposes.'
    )
    main_heading = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        help_text='The main heading of the step-by-step guide.'
    )
    main_content = models.TextField(
        null=True,
        blank=True,
        help_text='The main content of the step-by-step guide.'
    )

    sub_fields_section = models.ManyToManyField(
        'SBSGuideSubSection', blank=True, help_text='The subsections for this step-by-step guide.')
    # Metadata

    class Meta:
        ordering = ['id']
        verbose_name = 'step-by-step guide'
        verbose_name_plural = 'step-by-step guides'
        db_table = 'step_by_step_guides_contact'


class SBSGuideSubSection(models.Model):
    """
    A model representing multiple subheadings and subcontents within a step-by-step guide.
    """
    # Fields
    parent_guide = models.ForeignKey(
        StepByStepGuid,
        on_delete=models.CASCADE,
        related_name='subsections',
        help_text='The parent step-by-step guide that this subsection belongs to.'
    )
    blog_post = models.ForeignKey(
        'ContactUs',
        on_delete=models.CASCADE,
        related_name='sbs_subsections',
        help_text='The contact us page that this subsection belongs to.'
    )
    sbs_index = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        help_text='The number of this subsection within the parent step-by-step guide.'
    )
    sub_headings_and_contents = models.ManyToManyField(
        'SubFields',
        related_name='sub_fields',
        help_text='The subcontents for this subsection.'
    )

    parent_subsection = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='subsections',
        on_delete=models.CASCADE,
        help_text='The parent subsection that this subsection belongs to.'
    )

    # Metadata

    class Meta:
        ordering = ['id']
        verbose_name = 'step-by-step guide subsection'
        verbose_name_plural = 'step-by-step guide subsections'
        db_table = 'step_by_step_guide_subsections_contact'


class SubFields(models.Model):
    sbs_guide_sub_section = models.ForeignKey(
        SBSGuideSubSection,
        on_delete=models.CASCADE,
        related_name='sub_fields_parent',
        help_text='The parent subsection that this subheading belongs to.'
    )
    sub_index = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        help_text='The number of this subsection within the parent step-by-step guide.'
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
