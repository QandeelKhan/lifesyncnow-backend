# Generated by Django 4.1.6 on 2023-07-08 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_author_earnings_view'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='paragraphs',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='quote',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='quote_writer',
        ),
    ]
