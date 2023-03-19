from django.urls import path
from .views import UserProfileView, UserProfileRetrieveUpdateDestroyView


urlpatterns = [
    # path('profile/', UserProfileListCreateView.as_view(),
    #      name='user-profile-list-create'),
    path('profile/', UserProfileView.as_view(),
         name='user-profile-list-create'),
    path('profile/<int:pk>/', UserProfileRetrieveUpdateDestroyView.as_view(),
         name='user-profile-retrieve-update-destroy'),
]
