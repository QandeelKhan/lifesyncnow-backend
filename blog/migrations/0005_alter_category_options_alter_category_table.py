# Generated by Django 4.1.6 on 2023-07-08 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_blogpost_post_images_delete_blogpostimage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('category_name',), 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelTable(
            name='category',
            table='category',
        ),
    ]