from rest_framework import serializers
from .models import PageTemplate, FollowUs


class FollowUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowUs
        fields = ('facebook_link', 'twitter_link', 'instagram_link',
                  'youtube_link', 'pinterest_link')


class PageTemplateSerializer(serializers.ModelSerializer):
    follow_us = FollowUsSerializer()

    class Meta:
        model = PageTemplate
        fields = ('logo_name', 'logo_description',
                  'logo_image', 'copyright', 'follow_us')
