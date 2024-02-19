from django.contrib import admin

from django.contrib import admin

from user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'is_active')