from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, request
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blog.models import Blog


# Create your views here.
class BlogCreateView(CreateView):
    model = Blog
    fields = ('name', 'description', 'image')
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
    template_name = 'OB2/blog_detail.html'


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ('name', 'description', 'image')
    template_name = 'OB2/create_blog.html'
    success_url = reverse_lazy("user:create")

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = 'OB2/delete_blog.html'
    success_url = reverse_lazy('blog:list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise Http404
        return self.object
