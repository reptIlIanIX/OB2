from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from blog.models import Blog


# Create your views here.
class BlogCreateView(CreateView):
    model = Blog
    fields = ('name', 'description')
    template_name = 'OB2/create_blog.html'
    success_url = reverse_lazy("user:success")