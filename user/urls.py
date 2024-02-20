from django.urls import path

from user.views import UserCreateView, CreateCheckoutSessionView, SuccessView, CancelView, PreView

urlpatterns = [path('', UserCreateView.as_view(), name='users'),
               path('create-checkout-session/<pk>', CreateCheckoutSessionView.as_view(), name='checkout'),
               path('success/', SuccessView.as_view(), name='success'),
               path('cancel/', CancelView.as_view(), name='cancel'),
               path('preview/', PreView.as_view(), name='preview')
               ]
