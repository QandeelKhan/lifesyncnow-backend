# Generated by Django 4.1.7 on 2023-03-20 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogstepbystepguide_list_style'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogstepbystepguide',
            name='list_style',
            field=models.CharField(blank=True, choices=[('simple', 'Simple'), ('bulleted', 'Bulleted'), ('numbered', 'Numbered'), ('asterisk', 'Asterisk')], default='simple', help_text='The list style of the paragraph.', max_length=50, null=True),
        ),
    ]
