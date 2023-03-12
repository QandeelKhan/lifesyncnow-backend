# Generated by Django 4.1.6 on 2023-03-12 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_subheading_sbs_heading_sub'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sbsguidesubsection',
            name='sub_heading',
            field=models.ManyToManyField(help_text='The subheadings for the step-by-step guide.', related_name='sbs_guide_sub_heading', to='blog.subheading'),
        ),
    ]
