from django.contrib import admin

from django.contrib import admin

import blog
from blog.models import Blog
from user.models import User

admin.site.register(Blog)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'is_active')
