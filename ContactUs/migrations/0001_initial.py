# Generated by Django 4.1.7 on 2023-03-20 15:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertiseWithWellPlusGood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='The title of the about page.', max_length=100)),
                ('content', models.TextField(blank=True, help_text='The content of the about page.', null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, help_text='The date and time when the contact us page was created.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='The date and time when the contact us post was last updated.')),
                ('author_advertise_well_good', models.ForeignKey(help_text='The author of the contact us page.', on_delete=django.db.models.deletion.CASCADE, related_name='advertise_well_good', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'contact us',
                'db_table': 'Advertise-with-well-plus-good',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='The title of the about page.', max_length=100)),
                ('content', models.TextField(blank=True, help_text='The content of the about page.', null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, help_text='The date and time when the contact us page was created.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='The date and time when the contact us post was last updated.')),
                ('author', models.ForeignKey(help_text='The author of the contact us page.', on_delete=django.db.models.deletion.CASCADE, related_name='contact_us', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'contact us',
                'db_table': 'contact_us',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paragraph_title', models.CharField(blank=True, help_text='The title of the clause..', max_length=255, null=True)),
                ('paragraph_content', models.TextField(blank=True, help_text='The content of the clause..', null=True)),
                ('order', models.PositiveIntegerField(blank=True, default=0, help_text='The order in which the clause should appear in the terms and conditions..', null=True)),
                ('advertise_with_us', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='advertise_with_us', to='ContactUs.advertisewithwellplusgood')),
                ('contact_us', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact_paragraphs', to='ContactUs.contactus')),
            ],
        ),
        migrations.CreateModel(
            name='StepByStepGuide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_style', models.CharField(blank=True, choices=[('simple', 'Simple'), ('bulleted', 'Bulleted'), ('numbered', 'Numbered'), ('asterisk', 'Asterisk')], default='simple', help_text='The list style of the paragraph.', max_length=50, null=True)),
                ('sbs_guide_number', models.PositiveSmallIntegerField(blank=True, help_text='Number of the step-by-step guides on a post. Can be used for multiple purposes.', null=True)),
                ('sub_heading', models.CharField(blank=True, help_text='The text of this subheading.', max_length=255, null=True)),
                ('sub_content', models.TextField(blank=True, help_text='The text of this subcontent.', null=True)),
                ('sbs_index', models.PositiveSmallIntegerField(blank=True, help_text='The number of this subsection within the parent step-by-step guide.', null=True)),
                ('blog_paragraphs', models.ForeignKey(blank=True, help_text='The blog post that this step-by-step guide belongs to.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_paragraphs', to='ContactUs.paragraph')),
                ('contact_us', models.ForeignKey(help_text='The blog post that this step-by-step guide belongs to.', on_delete=django.db.models.deletion.CASCADE, related_name='step_by_step_guides_contact_specific', to='ContactUs.contactus')),
                ('sbs_self_refer', models.ForeignKey(blank=True, help_text='The parent subsection that this subsection belongs to.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sbsguides', to='ContactUs.stepbystepguide')),
            ],
            options={
                'verbose_name': 'step-by-step guide',
                'verbose_name_plural': 'step-by-step guides',
                'db_table': 'step_by_step_guides_contact_us_specific',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='paragraph',
            name='step_by_step_guide',
            field=models.ManyToManyField(blank=True, related_name='posts_sbs', to='ContactUs.stepbystepguide'),
        ),
        migrations.AddField(
            model_name='contactus',
            name='paragraphs',
            field=models.ManyToManyField(blank=True, null=True, related_name='paragraphs', to='ContactUs.paragraph'),
        ),
        migrations.AddField(
            model_name='advertisewithwellplusgood',
            name='paragraphs_advertise_well_good',
            field=models.ManyToManyField(blank=True, null=True, related_name='paragraphs_advertise_well_good', to='ContactUs.paragraph'),
        ),
    ]
