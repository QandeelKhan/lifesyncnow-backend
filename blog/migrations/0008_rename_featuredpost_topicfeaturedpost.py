# Generated by Django 4.1.7 on 2023-03-27 03:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_category_categorized_topics'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FeaturedPost',
            new_name='TopicFeaturedPost',
        ),
    ]