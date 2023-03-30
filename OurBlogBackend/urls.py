from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('UserManagement.urls')),
    path('api/', include('blog.urls')),
    path('api/', include('legal.urls')),
    path('api/', include('ContactUs.urls')),
    path('api/', include('UserProfile.urls')),
    path('api/', include('PageTemplate.urls')),
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.authtoken')),
    # django all auth
    # path('accounts/', include('allauth.urls')),
    # path('accounts-google/', include('allauth.socialaccount.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
