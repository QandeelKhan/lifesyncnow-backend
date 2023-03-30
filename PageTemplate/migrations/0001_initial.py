# Generated by Django 4.1.7 on 2023-03-30 17:47

import PageTemplate.models
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FollowUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook_link', models.CharField(blank=True, max_length=255, null=True)),
                ('twitter_link', models.CharField(blank=True, max_length=255, null=True)),
                ('instagram_link', models.CharField(blank=True, max_length=255, null=True)),
                ('youtube_link', models.CharField(blank=True, max_length=255, null=True)),
                ('pinterest_link', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PageTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo_name', models.CharField(blank=True, max_length=255, null=True)),
                ('logo_description', models.CharField(blank=True, max_length=255, null=True)),
                ('logo_image', models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='space-our-blog-backend/media'), upload_to='template-images/', validators=[PageTemplate.models.validate_image])),
                ('copyright', models.CharField(blank=True, max_length=255, null=True)),
                ('follow_us', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='follow_us_page_template', to='PageTemplate.followus')),
            ],
        ),
    ]