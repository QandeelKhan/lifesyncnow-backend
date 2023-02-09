from django.contrib import admin
from django.urls import path, include


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
]
