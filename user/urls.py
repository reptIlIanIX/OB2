from django.urls import path

from user.views import UserCreateView, CreateCheckoutSessionView, SuccessView, CancelView, PreView

app_name = 'user'


urlpatterns = [path('', UserCreateView.as_view(), name='create'),
               # path('view/<int:pk>', User),
               # path('edit/<int:pk>', User),
               # path('delete<int:pk>', User),
               # path('update/<int:pk>', User),
               path('create-checkout-session/', CreateCheckoutSessionView.as_view(), name='checkout'),
               path('success/', SuccessView.as_view(), name='success'),
               path('cancel/', CancelView.as_view(), name='cancel'),
               path('preview/', PreView.as_view(), name='preview')
               ]
