from django.urls import path

from blog.views import (BlogCreateView, BlogListView,
                        BlogDetailView, BlogUpdateView, BlogDeleteView)

app_name = 'blog'


urlpatterns = [path('create/',
                    BlogCreateView.as_view(), name='create_blog'),
               path('', BlogListView.as_view(), name='list'),
               path('detail/<int:pk>/',
                    BlogDetailView.as_view(), name='detail'),
               path('edit/<int:pk>/',
                    BlogUpdateView.as_view(), name='update'),
               path('delete/<int:pk>/',
                    BlogDeleteView.as_view(), name='delete'),]
