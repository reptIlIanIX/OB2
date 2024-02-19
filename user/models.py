from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(models.Model):
    name = models.CharField(max_length=20, verbose_name='имя')
    number = PhoneNumberField()
