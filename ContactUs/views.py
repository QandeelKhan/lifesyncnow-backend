from rest_framework import generics
from .models import ContactUs
from .serializers import ContactUsSerializer


class ContactUsList(generics.ListAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
