from django.contrib import admin

from django.contrib import admin

from user.models import User


@admin.register(User)
class ContactAdmin(admin.ModelAdmin):
    pass