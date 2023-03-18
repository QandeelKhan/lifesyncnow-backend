from rest_framework import generics
from .models import TermsAndConditions, Clause, UserAgreement
from .serializers import TermsAndConditionsSerializer, ClauseSerializer, UserAgreementSerializer


class TermsAndConditionsList(generics.ListCreateAPIView):
    queryset = TermsAndConditions.objects.all()
    serializer_class = TermsAndConditionsSerializer


class TermsAndConditionsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TermsAndConditions.objects.all()
    serializer_class = TermsAndConditionsSerializer


class ClauseList(generics.ListCreateAPIView):
    queryset = Clause.objects.all()
    serializer_class = ClauseSerializer


class ClauseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clause.objects.all()
    serializer_class = ClauseSerializer


class UserAgreementList(generics.ListCreateAPIView):
    queryset = UserAgreement.objects.all()
    serializer_class = UserAgreementSerializer


class UserAgreementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAgreement.objects.all()
    serializer_class = UserAgreementSerializer
