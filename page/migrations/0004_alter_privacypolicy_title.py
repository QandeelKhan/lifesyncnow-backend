# Generated by Django 4.1.6 on 2023-07-06 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_remove_privacypolicy_paragraphs_privacy_policy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='privacypolicy',
            name='title',
            field=models.CharField(help_text='The title of the Privacy Policy page.', max_length=100),
        ),
    ]
