from rest_framework import generics
from .models import ContactUs, AdvertiseWithWellPlusGood, PrivacyPolicy
from .serializers import ContactUsSerializer, AdvertiseWithWellPlusGoodSerializer, PrivacyPolicySerializer
from .paragraph_with_sbs import Paragraph


class ContactUsList(generics.ListAPIView):
    # queryset = Paragraph.objects.all()
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer


class AdvertiseWithWellPlusGoodListView(generics.ListAPIView):
    # queryset = Paragraph.objects.all()
    queryset = AdvertiseWithWellPlusGood.objects.all()
    serializer_class = AdvertiseWithWellPlusGoodSerializer


class PrivacyPolicyListView(generics.ListAPIView):
    # queryset = Paragraph.objects.all()
    queryset = PrivacyPolicy.objects.all()
    serializer_class = PrivacyPolicySerializer
