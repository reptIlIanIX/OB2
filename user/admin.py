from django.contrib import admin

from blog.models import Blog
from user.models import User

admin.site.register(Blog)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('number', 'first_name', 'is_active')
