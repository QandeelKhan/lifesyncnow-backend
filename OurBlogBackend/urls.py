from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('UserManagement.urls')),
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.authtoken')),
    # django all auth
    # path('accounts/', include('allauth.urls')),
    # path('accounts-google/', include('allauth.socialaccount.urls')),
]
