from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(models.Model):
    number = PhoneNumberField(verbose_name='телефон')
    name = models.CharField(max_length=20, verbose_name='имя')
    password = models.CharField(max_length=30, verbose_name="пароль")
    is_active = models.BooleanField(default=False, verbose_name="активация")
