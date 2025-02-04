import stripe
import json
from PIL.features import check
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, TemplateView, UpdateView
import logging

from flask import Flask, jsonify
from rest_framework import request

import user
from OB2 import settings
from user.forms import RegisterForm, UserUpdateForm
from user.models import User

stripe.api_key = settings.STRIPE_SECRET_KEY

logger = logging.getLogger(__name__)
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.INFO, filemode='a')


class PreView(TemplateView):
    """превьюшка перед оплатой и кнопка с оплатой"""

    template_name = 'OB2/home.html'


class UserCreateView(CreateView):
    """создание профиля"""

    model = User
    form_class = RegisterForm
    template_name = 'OB2/auth_form.html'
    success_url = reverse_lazy('user:create')


class ProfileView(UpdateView):
    """подробности профиля"""
    model = User
    form_class = UserUpdateForm
    template_name = 'OB2/update.html'
    success_url = reverse_lazy('user:create')

    def get_object(self, queryset=None):
        return self.request.user


def denied(request):
    """вьюшка для ограничений в доступе"""

    return render(request, 'OB2/Denied.html')


class SuccessView(TemplateView):
    """вьюшка с темплейтом при успехе оплаты на
    stripe(success_url думал как редирект сработает)"""

    template_name = 'OB2/success.html'
    success_url = reverse_lazy('blog:create_blog')


class CancelView(TemplateView):
    """вюшка с темплейтом при отмене оплаты на stripe"""
    template_name = 'OB2/cancelled.html'


class CreateCheckoutSessionView(View):
    '''создание сессии Stripe'''

    def post(self, request, *args, **kwargs):
        YOUR_DOMAIN = 'http://127.0.0.1:8000'
        try:
            checkout_session = stripe.checkout.Session.create(
                line_items=[
                    {
                        # Provide the exact Price ID
                        # (for example, pr_1234)
                        # of the product you want to sell
                        'price': 'price_1Olb7SErirJAHiVXsiaCqWNC',
                        'quantity': 1,
                    },
                ],
                mode='payment',

                client_reference_id=request.user.id if request.user.is_authenticated else None,
                success_url=YOUR_DOMAIN + '/success/',
                cancel_url=YOUR_DOMAIN + '/cancel/',
            )



        except Exception as e:
            return str(e)

        return redirect(checkout_session.url, code=303)


@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def stripe_webhook_view(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = 'whsec_8891e7456cf6c6f69b1dc6d2c5b98b5e54ebf294558d9c904c43acc778012b11'
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']

    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        print('Error parsing payload: {}'.format(str(e)))
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        print('Error verifying webhook signature: {}'.format(str(e)))
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event.type == 'checkout.session.completed':
        # Retrieve the session. If you require line items in the response, you may include them by expanding line_items.
        customer_email = event.data.object['customer_details']['email']
        email_user = User.objects.get(email=customer_email)
        email_user.is_subscribed = True
        email_user.save()
    else:
        print('Unhandled event type {}'.format(event['type']))

    return HttpResponse(status=200)


