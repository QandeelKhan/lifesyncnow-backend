from django.urls import path
from .views import ContactUsList, AdvertiseWithWellPlusGoodListView, PrivacyPolicyListView

urlpatterns = [
    path('contact-us/', ContactUsList.as_view(), name='contact-us-list'),
    path('Advertise-With-Well-Plus-Good/',
         AdvertiseWithWellPlusGoodListView.as_view(), name='advertise-us-list'),
    path('privacy/',
         PrivacyPolicyListView.as_view(), name='privacy-policy'),
]
