from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseNotAllowed, HttpResponse, HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic import (CreateView, ListView,
                                  DetailView, UpdateView, DeleteView)
from dns.rdtypes.IN.HTTPS import HTTPS
from rest_framework.exceptions import PermissionDenied
from rest_framework.status import HTTP_401_UNAUTHORIZED
from starlette.status import HTTP_403_FORBIDDEN

from blog.models import Blog


# Create your views here.
class BlogCreateView(CreateView):
    """Для создания блога"""
    model = Blog
    fields = ('name', 'description', 'image')
    template_name = 'OB2/create_blog.html'
    success_url = reverse_lazy("user:create")

    def form_valid(self, form):
        """сохраняет user как owner после создания
        блога (присваивание id)"""
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class BlogListView(ListView):
    """список блогов"""
    model = Blog
    template_name = 'OB2/blog_list.html'


class BlogDetailView(DetailView):
    """подробно посмотреть блог"""
    model = Blog
    template_name = 'OB2/blog_detail.html'


not_authorized = HttpResponseNotAllowed("Not allowed")


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    """обновление блога после создания"""
    model = Blog
    fields = ('name', 'description', 'image')
    template_name = 'OB2/update_blog.html'
    success_url = reverse_lazy("user:create")

    def get_object(self, queryset=None):
        """обновлять блог может только создатель"""
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise PermissionDenied
        return self.object


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    """'удаление блога """
    model = Blog
    template_name = 'OB2/delete_blog.html'
    success_url = reverse_lazy('blog:list')

    def get_object(self, queryset=None):
        """удалить блог может только создатель"""

        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user:
            raise PermissionDenied
        return self.object
