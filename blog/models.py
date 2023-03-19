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
# for more then one images and image_links we created BlogPostImage model


class BlogPostImage(models.Model):
    images = models.ImageField(upload_to='blog-images/',
                               storage=fs, validators=[validate_image], blank=True, null=True)
    # image_links = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return str(self.images)


class BlogStepByStepGuide(models.Model):
    """
    A model representing a step-by-step guide within a blog post.
    """
    # Fields
    blog_post = models.ForeignKey(
        'BlogPost',
        on_delete=models.CASCADE,
        related_name='step_by_step_guides',
        help_text='The blog post that this step-by-step guide belongs to.'
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
        db_table = 'step_by_step_guides'


class SBSGuideSubSection(models.Model):
    """
    A model representing multiple subheadings and subcontents within a step-by-step guide.
    """
    # Fields
    parent_guide = models.ForeignKey(
        BlogStepByStepGuide,
        on_delete=models.CASCADE,
        related_name='subsections',
        help_text='The parent step-by-step guide that this subsection belongs to.'
    )
    blog_post = models.ForeignKey(
        'BlogPost',
        on_delete=models.CASCADE,
        related_name='sbs_subsections',
        help_text='The blog post that this subsection belongs to.'
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
    # sub_headings_and_contents = models.ManyToManyField(
    #     'SubFields',
    #     related_name='sub_fields',
    #     help_text='The subcontents for this subsection.'
    # )
    # ForeignKey to itself
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
        db_table = 'step_by_step_guide_subsections'


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


class BlogPost(models.Model):
    step_by_step_guide = models.ManyToManyField(
        BlogStepByStepGuide, related_name='blog_posts', blank=True)
    title = models.CharField(
        max_length=100, help_text="The title of the blog post.")
    content = models.TextField(
        null=True, blank=True, help_text="The title of the blog post.")

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
        'BlogParagraph', related_name='paragraphs')
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

    # def save(self, *args, **kwargs):
    # # check if the post is being marked as a featured post
    #     if self.featured_posts:
    #         # count how many featured posts already exist for this category
    #         num_featured_posts = BlogPost.objects.filter(
    #         category=self.category, featured_posts=True).count()

    #     # if there are already three featured posts for this category, raise an exception
    #     if num_featured_posts >= 3:
    #         raise ValueError("A maximum of three posts can be marked as featured posts for each category.")

    #     super().save(*args, **kwargs)


class BlogParagraph(models.Model):
    """
    Model representing a clause within the terms and conditions.
    """
    blog_post = models.ForeignKey(
        'BlogPost', on_delete=models.CASCADE, related_name='blog_paragraphs', blank=True, null=True)
    paragraph_title = models.CharField(
        max_length=255, help_text='The title of the clause..', null=True, blank=True)
    paragraph_content = models.TextField(null=True, blank=True,
                                         help_text='The content of the clause..')
    order = models.PositiveIntegerField(default=0,
                                        help_text='The order in which the clause should appear in the terms and conditions..', blank=True, null=True)

    # class Meta:
    #     ordering = ['order']

    def __str__(self):
        return self.paragraph_title

    # Metadata
    # class Meta:
    #     ordering = ['id']
    #     verbose_name = 'BlogParagraph'
    #     verbose_name_plural = 'BlogParagraphs'
    #     db_table = 'BlogParagraphs'


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
