# Generated by Django 4.1.7 on 2023-03-26 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_featuredpost_featured_topic_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='categorized_topics',
            field=models.ManyToManyField(blank=True, related_name='categorized_topic', to='blog.topictype'),
        ),
    ]
