from django.db import models
from django.core.files.storage import default_storage
from decouple import config
from django.core.files.storage import FileSystemStorage
from PIL import Image

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


class BlogStepByStepGuide(models.Model):
    """
    A model representing a step-by-step guide within a blog post.
    """
    # Fields
    SIMPLE = 'simple'
    BULLETED = 'bulleted'
    NUMBERED = 'numbered'
    ASTERISK = 'asterisk'
    STYLES_CHOICES = [
        (SIMPLE, 'Simple'),
        (BULLETED, 'Bulleted'),
        (NUMBERED, 'Numbered'),
        (ASTERISK, 'Asterisk'),
        # Add more choices as needed
    ]
    list_style = models.CharField(max_length=50, choices=STYLES_CHOICES, default=SIMPLE,
                                  help_text='The list style of the paragraph.', null=True, blank=True,)
    blog_post = models.ForeignKey(
        'BlogPost',
        on_delete=models.CASCADE,
        related_name='step_by_step_guides',
        help_text='The blog post that this step-by-step guide belongs to.'
    )
    blog_paragraphs = models.ForeignKey(
        'BlogParagraph',
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
    sbs_image = models.ImageField(upload_to='blog-images/sbs-guide-images',
                                  storage=fs, validators=[validate_image], blank=True, null=True)

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
        db_table = 'step_by_step_guides'


class BlogParagraph(models.Model):
    """
    Model representing a clause within the terms and conditions.
    """
    blog_post = models.ForeignKey(
        'BlogPost', on_delete=models.CASCADE, related_name='blog_paragraphs', blank=True, null=True)
    paragraph_title = models.CharField(
        max_length=255, help_text='The title of the clause..', null=True, blank=True)
    paragraph_image = models.ImageField(upload_to='blog-images/paragraph-images',
                                        storage=fs, validators=[validate_image], blank=True, null=True)
    paragraph_content = models.TextField(null=True, blank=True,
                                         help_text='The content of the clause..')
    step_by_step_guide = models.ManyToManyField(
        'BlogStepByStepGuide', related_name='blog_posts_sbs', blank=True)
    order = models.PositiveIntegerField(default=0,
                                        help_text='The order in which the clause should appear in the terms and conditions..', blank=True, null=True)

    paragraphs_self_refer = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='paragraph_self_refer',
        on_delete=models.CASCADE,
        help_text='The parent subsection that this subsection belongs to.'
    )
    # class Meta:
    #     ordering = ['order']

    def __str__(self):
        return self.paragraph_title
