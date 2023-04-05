from rest_framework import serializers
from .models import ContactUs, AdvertiseWithWellPlusGood, PrivacyPolicy
from .paragraph_with_sbs import Paragraph, StepByStepGuide


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


class PrivacyPolicySerializer(serializers.ModelSerializer):
    paragraphs_privacy_policy = ParagraphSerializer(many=True)

    class Meta:
        model = PrivacyPolicy
        fields = '__all__'
