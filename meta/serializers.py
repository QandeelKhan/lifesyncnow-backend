from rest_framework import serializers
from meta.models import SEO


class SEOSerializer(serializers.ModelSerializer):
    class Meta:
        model = SEO
        fields = ('meta_title', 'meta_description', 'meta_keywords')
