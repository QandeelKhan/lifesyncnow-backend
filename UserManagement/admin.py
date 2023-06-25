# from django.contrib import admin
# from UserManagement.models import User
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# class UserAdmin(BaseUserAdmin):
#     # The fields to be used in displaying the User model.
#     # These override the definitions on the base UserModelAdmin
#     # that reference specific fields on auth.User.
#     list_display = ('id', 'email', 'first_name', 'last_name',
#                     'tc', 'is_admin', 'user_slug')
#     list_filter = ('is_admin',)
#     fieldsets = (
#         ('User Credentials', {'fields': ('email', 'password')}),
#         ('Personal info', {
#          'fields': ('first_name', "last_name", 'tc', 'user_slug', 'profile_image')}),
#         ('Permissions', {'fields': ('is_admin',)}),
#     )
#     # add_fieldsets is not a standard ModelAdmin attribute. UserModelAdmin
#     # overrides get_fieldsets to use this attribute when creating a user.
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'first_name', 'last_name', 'tc', 'password1', 'password2'),
#         }),
#     )
#     search_fields = ('email',)
#     ordering = ('email', 'id')
#     filter_horizontal = ()


# # Now register the new UserAdmin...
# admin.site.register(User, UserAdmin)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'tc', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, CustomUserAdmin)
