from django.contrib import admin
from .models import UserInfo
# Register your models here.

@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'username',  'email', 'is_active', 'is_superuser']


