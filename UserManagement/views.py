from django.http import JsonResponse
from .models import User


def get_user_details(request, user_id):
    user = User.objects.get(id=user_id)
    data = {
        'id': user.id,
        'username': user.username,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
    }
    return JsonResponse(data)
