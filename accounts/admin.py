from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

#MODEL
from .models import (
    CustomUser
)
# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ['id', 'username', 'gender']
    list_display_links = ['id', 'username']
admin.site.register(CustomUser,CustomUserAdmin)


