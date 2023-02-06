# from django.urls import path
# from .views import LoginView, SignupView, UserViewSet

# urlpatterns = [
#     path('user/<int:user_id>/', UserViewSet.as_view({'get': 'retrieve'}), name='get_user_details'),
#     path('user/login/', LoginView.as_view(), name='login'),
#     path('user/signup/', SignupView.as_view(), name='signup'),
#     path('user/logout/', UserViewSet.as_view({'post': 'logout'}), name='logout'),
# ]


from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('changepassword/', views.UserChangePasswordView.as_view(),
         name='changepassword'),
    path('send-reset-password-email/', views.SendPasswordResetEmailView.as_view(),
         name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', views.UserPasswordResetView.as_view(),
         name='reset-password'),
]
