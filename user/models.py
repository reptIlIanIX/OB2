from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(models.Model):
    number = PhoneNumberField()
    name = models.CharField(max_length=20, verbose_name='имя')
    is_active = models.BooleanField(default=False, verbose_name="активация")