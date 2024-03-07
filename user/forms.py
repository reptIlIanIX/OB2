from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from user.models import User


class RegisterForm(UserCreationForm):
    # Наследуемся от специальной формы UserCreationForm из модуля auth
    class Meta:
        model = User
        fields = ('number', 'password1', 'password2')


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'number')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()
