from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

urlpatterns = [
    path('user/register/', views.UserRegistrationView.as_view(), name='register'),
    path('user/login/', views.UserLoginView.as_view(), name='login'),
    path('user/profile/', views.UserProfileView.as_view(), name='profile'),
    path('changepassword/', views.UserChangePasswordView.as_view(),
         name='changepassword'),
    path('send-reset-password-email/', views.SendPasswordResetEmailView.as_view(),
         name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', views.UserPasswordResetView.as_view(),
         name='reset-password'),
    path('user/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('user/token/refresh/',
         TokenRefreshView.as_view(), name='token_refresh'),
]
