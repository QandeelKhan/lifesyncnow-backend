# Generated by Django 4.1.7 on 2023-04-05 18:07

import UserProfile.models
from django.conf import settings
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255)),
                ('email', models.EmailField(blank=True, max_length=255, null=True, unique=True, verbose_name='Email')),
                ('user_slug', models.SlugField(blank=True, help_text="A URL-friendly version of the blog post's title.", max_length=255, null=True, unique=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('profile_image', models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='space-our-blog-backend/media'), upload_to='profile-images/', validators=[UserProfile.models.validate_image])),
                ('country', models.CharField(blank=True, max_length=150, null=True)),
                ('city', models.CharField(blank=True, max_length=150, null=True)),
                ('twitter_acc', models.CharField(blank=True, max_length=300, null=True)),
                ('facebook_acc', models.CharField(blank=True, max_length=300, null=True)),
                ('instagram_acc', models.CharField(blank=True, max_length=300, null=True)),
                ('role', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_role', to='UserProfile.role')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
