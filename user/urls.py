from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from user import views
from user.views import (UserCreateView, CreateCheckoutSessionView, SuccessView,
                        CancelView, PreView, ProfileView)

app_name = 'user'

urlpatterns = [path('', UserCreateView.as_view(), name='create'),
               path('login/',
                    LoginView.as_view(template_name='OB2/login.html'),
                    name='login'),
               path('logout/', LogoutView.as_view(), name='logout'),
               path('create-checkout-session/',
                    CreateCheckoutSessionView.as_view(), name='checkout'),
               path('success/', SuccessView.as_view(), name='success'),
               path('cancel/', CancelView.as_view(), name='cancel'),
               path('preview/', PreView.as_view(), name='preview'),
               path('profile/', ProfileView.as_view(), name='profile'),
               path('denied/', views.denied, name='denied'),
               path('config/', views.stripe_config),
               path('webhook/', views.stripe_webhook_view),  # new

               ]
