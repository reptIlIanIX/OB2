from django import forms
from django.contrib.auth.forms import UserCreationForm

from user.models import User

from phonenumber_field.formfields import PhoneNumberField



class RegisterForm(UserCreationForm):
    # Наследуемся от специальной формы UserCreationForm из модуля auth
    class Meta:
        model = User
        fields = ('number', 'password1', 'password2')

