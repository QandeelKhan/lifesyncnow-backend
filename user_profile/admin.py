from django.contrib import admin
from .models import UserProfile, Role


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'role', 'country', 'city']
    search_fields = ['user__email', 'user__username',
                     'user__first_name', 'user__last_name']
    list_filter = ['role', 'country', 'city']
    autocomplete_fields = ['user']
    ordering = ['-id']


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Role)
