import stripe
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, TemplateView, UpdateView

from OB2 import settings
from user.forms import RegisterForm, UserUpdateForm
from user.models import User

stripe.api_key = settings.STRIPE_SECRET_KEY


class PreView(TemplateView):
    template_name = 'OB2/home.html'


class UserCreateView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'OB2/auth_form.html'
    success_url = reverse_lazy('user:preview')


class ProfileView(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'OB2/update.html'
    success_url = reverse_lazy('user:create')

    def get_object(self, queryset=None):
        return self.request.user


def denied(request):
    return render(request, 'OB2/Denied.html')


class SuccessView(TemplateView):
    template_name = 'OB2/success.html'
    success_url = reverse_lazy('blog:create_blog')


class CancelView(TemplateView):
    template_name = 'OB2/cancelled.html'


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        # user_id = self.kwargs['pk']
        # user = User.objects.get(pk=user_id)
        YOUR_DOMAIN = 'http://127.0.0.1:8000'
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                        'price': 'price_1Olb7SErrJAHiVXsiaCqWNC',
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url=YOUR_DOMAIN + '/success/',
                cancel_url=YOUR_DOMAIN + '/cancel/',
            )
        except Exception as e:
            return str(e)

        return redirect(checkout_session.url, code=303)
