from rest_framework import generics
from .models import ContactUs
from .serializers import ContactUsSerializer
from .paragraph_with_sbs import Paragraph


class ContactUsList(generics.ListAPIView):
    # queryset = Paragraph.objects.all()
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
