from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import MyUser
# Register your models here.


# class CustomUserAdmin(UserAdmin):
#     fieldsets = (
#         *UserAdmin.fieldsets,
#         (
#             'Permissions',
#             {
#                 'fields':(
#                     'is_seller',
#                 )

#             }
#         )
#     )
# admin.site.register(User, CustomUserAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_seller')
    fieldsets = (
        (('Personal info', {'fields': ('first_name', 'last_name', 'email')}), 
        ('Permissions', {'fields': ('is_seller','is_active')}))
    )
admin.site.register(MyUser, UserAdmin)
# @admin.register(User)

