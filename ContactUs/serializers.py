from rest_framework import serializers
from .models import ContactUs, Paragraph


class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = ('id', 'paragraph_title', 'paragraph_content')


class ContactUsSerializer(serializers.ModelSerializer):
    paragraphs = ParagraphSerializer(
        source='contact_paragraphs.all', many=True)

    class Meta:
        model = ContactUs
        fields = ('id', 'title', 'content', 'author',
                  'created_at', 'updated_at', 'paragraphs',)
