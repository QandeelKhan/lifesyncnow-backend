from django.urls import path, include
from . import views

urlpatterns = [
    path('user/register/', views.UserRegistrationView.as_view(), name='register'),
    path('user/login/', views.UserLoginView.as_view(), name='login'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('changepassword/', views.UserChangePasswordView.as_view(),
         name='changepassword'),
    path('send-reset-password-email/', views.SendPasswordResetEmailView.as_view(),
         name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', views.UserPasswordResetView.as_view(),
         name='reset-password'),
    #
    #     path('accounts/', include('allauth.urls')),
    #     path('accounts-google/', include('allauth.socialaccount.urls')),
    #     path('google-login/', views.GoogleLogin.as_view(), name='google-login'),

]
