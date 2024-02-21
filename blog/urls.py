from django.urls import path

from blog.views import BlogCreateView

app_name = 'blog'


urlpatterns = [path('create/', BlogCreateView.as_view(), name='create_blog'),]
