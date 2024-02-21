from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    number = models.CharField(max_length=13, verbose_name='телефон', unique=True)
    name = models.CharField(max_length=50, verbose_name='имя')


    USERNAME_FIELD = 'number'
    REQUIRED_FIELDS = []