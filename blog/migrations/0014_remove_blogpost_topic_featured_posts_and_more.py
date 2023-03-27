# Generated by Django 4.1.7 on 2023-03-27 04:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_topicfeaturedpost_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='topic_featured_posts',
        ),
        migrations.AlterField(
            model_name='topicfeaturedpost',
            name='featured_topic_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='featured_posts', to='blog.topictype'),
        ),
    ]
