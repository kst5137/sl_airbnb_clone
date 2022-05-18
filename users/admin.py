from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from django.contrib.auth.admin import UserAdmin


UserAdmin.fieldsets += (("Custom fields", {"fields": ("u_phonenum","u_address","SEX")}),)


#
# fieldsets = UserAdmin.fieldsets + (
#         (None, {'fields': ('u_phonenum', 'u_address','SEX')}),
#     )
# admin.site.register(User, UserAdmin)