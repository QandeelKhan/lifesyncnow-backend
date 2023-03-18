from rest_framework import serializers
from .models import TermsAndConditions, Clause, UserAgreement


class ClauseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clause
        fields = '__all__'


class TermsAndConditionsSerializer(serializers.ModelSerializer):
    clauses = ClauseSerializer(many=True, read_only=True)

    class Meta:
        model = TermsAndConditions
        fields = '__all__'


class UserAgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAgreement
        fields = '__all__'
