from django.urls import path

from blog.views import BlogCreateView, BlogListView, BlogDetailView

app_name = 'blog'


urlpatterns = [path('create/', BlogCreateView.as_view(), name='create_blog'),
               path('', BlogListView.as_view(), name='list'),
               path('detail', BlogDetailView.as_view(), name='list')]
]