from django.shortcuts import render
from django.views.generic import ListView, CreateView

from user.models import User


class UserCreateView(CreateView):
    model = User
    fields = ('number',)
    template_name = 'OB2/auth_form.html'
