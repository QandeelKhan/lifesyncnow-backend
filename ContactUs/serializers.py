from rest_framework import serializers
from .models import ContactUs
from .paragraph_with_sbs import Paragraph, StepByStepGuide


class StepByStepGuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = StepByStepGuide
        fields = '__all__'


class ParagraphSerializer(serializers.ModelSerializer):
    step_by_step_guide = StepByStepGuideSerializer(
        source='blog_paragraphs.all', many=True)

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
