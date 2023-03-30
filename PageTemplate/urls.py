from django.urls import path
from .views import PageTemplateList, PageTemplateDetail

urlpatterns = [
    path('page-templates/', PageTemplateList.as_view(), name='page-template-list'),
    path('page-templates/<int:pk>/', PageTemplateDetail.as_view(),
         name='page-template-detail'),
]
