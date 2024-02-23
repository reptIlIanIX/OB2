from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from blog.models import Blog


# Create your views here.
class BlogCreateView(CreateView):
    model = Blog
    fields = ('name', 'description')
    template_name = 'OB2/create_blog.html'
    success_url = reverse_lazy("user:create")

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)

class BlogListView(ListView):
    model = Blog
    template_name = 'OB2/blog_list.html'


class BlogDetailView(DetailView):
    model = Blog

