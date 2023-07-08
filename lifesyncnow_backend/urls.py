from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from ckeditor_uploader.views import ImageUploadView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('user_management.urls')),
    path('api/', include('blog.urls')),
    path('api/', include('legal.urls')),
    path('api/', include('page.urls')),
    path('api/', include('user_profile.urls')),
    path('api/', include('global_content.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('uploads/', ImageUploadView.as_view(), name="uploads"),
    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.authtoken')),
    # django all auth
    # path('accounts/', include('allauth.urls')),
    # path('accounts-google/', include('allauth.socialaccount.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


def get_filename(filename, request):
    return filename.upper()


# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
