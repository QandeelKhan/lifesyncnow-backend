# Generated by Django 4.1.6 on 2023-07-06 11:55

import blog.models
import blog.paragraph_with_sbs
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogParagraph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paragraph_title', models.CharField(blank=True, help_text='The title of the clause..', max_length=255, null=True)),
                ('paragraph_image', models.ImageField(blank=True, null=True, upload_to='blog-images/paragraph-images', validators=[blog.paragraph_with_sbs.validate_image])),
                ('paragraph_content', models.TextField(blank=True, help_text='The content of the clause..', null=True)),
                ('order', models.PositiveIntegerField(blank=True, default=0, help_text='The order in which the clause should appear in the terms and conditions..', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='The title of the blog post.', max_length=100)),
                ('content', models.TextField(blank=True, help_text='The title of the blog post.', null=True)),
                ('status', models.IntegerField(blank=True, choices=[(0, 'Draft'), (1, 'Publish')], default=0, null=True)),
                ('slug', models.SlugField(blank=True, help_text="A URL-friendly version of the blog post's title.", max_length=255, null=True, unique=True)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='blog-images/', validators=[blog.models.validate_image])),
                ('quote', models.CharField(blank=True, max_length=255, null=True)),
                ('quote_writer', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, help_text='The date and time when the blog post was created.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='The date and time when the blog post was last updated.')),
                ('most_recent_posts', models.BooleanField(blank=True, default=False, null=True)),
                ('featured_posts', models.BooleanField(blank=True, default=False, null=True)),
                ('older_posts', models.BooleanField(blank=True, default=False, null=True)),
                ('author', models.ForeignKey(help_text='The author of the blog post.', on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
                ('author_profile', models.ForeignKey(blank=True, help_text='The author of the blog post.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to='user_profile.userprofile')),
            ],
            options={
                'verbose_name_plural': 'blog posts',
                'db_table': 'blog_posts',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='BlogPostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, null=True, upload_to='blog-images/', validators=[blog.models.validate_image])),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('category_slug', models.SlugField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('comment_text', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.blogpost')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(blank=True, max_length=100, null=True)),
                ('topic_slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='blog.category')),
            ],
        ),
        migrations.CreateModel(
            name='TopicFeaturedPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('featured_topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='featured_posts', to='blog.topic')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='featured_in', to='blog.blogpost')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('reply_text', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to=settings.AUTH_USER_MODEL)),
                ('comment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='blog.comment')),
            ],
        ),
        migrations.CreateModel(
            name='BlogStepByStepGuide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_style', models.CharField(blank=True, choices=[('simple', 'Simple'), ('bulleted', 'Bulleted'), ('numbered', 'Numbered'), ('asterisk', 'Asterisk')], default='simple', help_text='The list style of the paragraph.', max_length=50, null=True)),
                ('sbs_guide_number', models.PositiveSmallIntegerField(blank=True, help_text='Number of the step-by-step guides on a post. Can be used for multiple purposes.', null=True)),
                ('sbs_image', models.ImageField(blank=True, null=True, upload_to='blog-images/sbs-guide-images', validators=[blog.paragraph_with_sbs.validate_image])),
                ('sub_heading', models.CharField(blank=True, help_text='The text of this subheading.', max_length=255, null=True)),
                ('sub_content', models.TextField(blank=True, help_text='The text of this subcontent.', null=True)),
                ('sbs_index', models.PositiveSmallIntegerField(blank=True, help_text='The number of this subsection within the parent step-by-step guide.', null=True)),
                ('blog_paragraphs', models.ForeignKey(blank=True, help_text='The blog post that this step-by-step guide belongs to.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_paragraphs', to='blog.blogparagraph')),
                ('blog_post', models.ForeignKey(help_text='The blog post that this step-by-step guide belongs to.', on_delete=django.db.models.deletion.CASCADE, related_name='step_by_step_guides', to='blog.blogpost')),
                ('sbs_self_refer', models.ForeignKey(blank=True, help_text='The parent subsection that this subsection belongs to.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sbsguides', to='blog.blogstepbystepguide')),
            ],
            options={
                'verbose_name': 'step-by-step guide',
                'verbose_name_plural': 'step-by-step guides',
                'db_table': 'step_by_step_guides',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_category', to='blog.category'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='paragraphs',
            field=models.ManyToManyField(related_name='paragraphs', to='blog.blogparagraph'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='post_images',
            field=models.ManyToManyField(blank=True, related_name='post_images', to='blog.blogpostimage'),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='blog.topic'),
        ),
        migrations.AddField(
            model_name='blogparagraph',
            name='blog_post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_paragraphs', to='blog.blogpost'),
        ),
        migrations.AddField(
            model_name='blogparagraph',
            name='paragraphs_self_refer',
            field=models.ForeignKey(blank=True, help_text='The parent subsection that this subsection belongs to.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='paragraph_self_refer', to='blog.blogparagraph'),
        ),
        migrations.AddField(
            model_name='blogparagraph',
            name='step_by_step_guide',
            field=models.ManyToManyField(blank=True, related_name='blog_posts_sbs', to='blog.blogstepbystepguide'),
        ),
    ]
