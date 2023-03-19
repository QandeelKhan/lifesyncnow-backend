from django.urls import path
from .views import ContactUsList

urlpatterns = [
    path('contact-us/', ContactUsList.as_view(), name='contact-us-list'),
]
