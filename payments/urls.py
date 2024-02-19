from django.urls import path

from payments.views import PaymentView

urlpatterns = [
    path('', PaymentView.as_view(), name='home'),
]