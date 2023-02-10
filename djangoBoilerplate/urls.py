from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('', include('UserManagement.urls')),
    path('api/', include('UserManagement.urls')),
    # django all auth
    # path('accounts/', include('allauth.urls')),
    # path('accounts-google/', include('allauth.socialaccount.urls')),
    # path('google-login/', views.GoogleLogin.as_view(), name='google-login'),
    path('api/user/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/user/token/refresh/',
         TokenRefreshView.as_view(), name='token_refresh'),
]
