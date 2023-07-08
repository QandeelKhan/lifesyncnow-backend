from rest_framework import serializers
from .models import ContactUs, AdvertiseWithWellPlusGood, PrivacyPolicy
from .paragraph_with_sbs import Paragraph, StepByStepGuide
from meta.serializers import SEOSerializer
from django.conf import settings
import re


class StepByStepGuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = StepByStepGuide
        fields = '__all__'


class ParagraphSerializer(serializers.ModelSerializer):
    step_by_step_guide = StepByStepGuideSerializer(many=True)

    class Meta:
        model = Paragraph
        fields = ('id', 'paragraph_title',
                  'paragraph_content', 'step_by_step_guide')


class ContactUsSerializer(serializers.ModelSerializer):
    paragraphs = ParagraphSerializer(
        source='contact_paragraphs.all', many=True)

    class Meta:
        model = ContactUs
        fields = ('id', 'title', 'content', 'author',
                  'created_at', 'updated_at', 'paragraphs',)


class AdvertiseWithWellPlusGoodSerializer(serializers.ModelSerializer):
    paragraphs_advertise_well_good = ParagraphSerializer(many=True)

    class Meta:
        model = AdvertiseWithWellPlusGood
        fields = '__all__'


SEARCH_PATTERN = 'href=\\"/media/ckeditor/'
SITE_DOMAIN = "http://127.0.0.1:8000"
REPLACE_WITH = 'href=\\"%s/media/ckeditor/' % SITE_DOMAIN


class FixAbsolutePathSerializer(serializers.Field):

    def to_representation(self, value):
        text = value.replace(SEARCH_PATTERN, REPLACE_WITH)
        return text


class FixImageUrlSerializerField(serializers.CharField):
    def to_representation(self, value):
        if value:
            # Regular expression to match image URLs
            pattern = r'<img[^>]*src="([^"]+)"[^>]*>'

            # Find all image URLs in the content field
            image_urls = re.findall(pattern, value)

            # Fix the image URLs by adding the server URL
            fixed_urls = [f'{settings.SERVER_URL}{url}' for url in image_urls]

            # Replace the image URLs in the content field
            for original_url, fixed_url in zip(image_urls, fixed_urls):
                value = value.replace(original_url, fixed_url)

        return value
    # def to_representation(self, value):
    #     if value:
    #         # Regular expression to match image URLs
    #         pattern = r'<img([^>]*)src=["\']([^"\']+)["\']([^>]*)>'

    #         # Find all image URLs in the content field
    #         matches = re.finditer(pattern, value)

    #         # Fix the image URLs by adding the server URL and new class
    #         for match in matches:
    #             attrs = match.group(1)
    #             url = match.group(2)
    #             end_attrs = match.group(3)

    #             # Check if 'class' attribute is present
    #             if 'class' not in attrs:
    #                 attrs += ' class="ck-content-img"'

    #             fixed_url = f'{settings.SERVER_URL}{url}'
    #             fixed_tag = f'<img{attrs} src="{fixed_url}"{end_attrs}>'

    #             value = value.replace(match.group(0), fixed_tag)

    #     return value


class PrivacyPolicySerializer(serializers.ModelSerializer):
    content = FixImageUrlSerializerField()

    class Meta:
        model = PrivacyPolicy
        fields = '__all__'
