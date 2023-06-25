from django.urls import path
from .views import SubscriberView

urlpatterns = [
    path('subscribe/', SubscriberView.as_view(), name='subscribe'),
]
