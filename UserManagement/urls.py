from django.urls import path

from . import views

urlpatterns = [
    path('user/<int:user_id>/', views.get_user_details, name='get_user_details'),
]
