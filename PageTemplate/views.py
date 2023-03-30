from rest_framework import generics
from .models import PageTemplate
from .serializers import PageTemplateSerializer


class PageTemplateList(generics.ListAPIView):
    queryset = PageTemplate.objects.all()
    serializer_class = PageTemplateSerializer


class PageTemplateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PageTemplate.objects.all()
    serializer_class = PageTemplateSerializer
