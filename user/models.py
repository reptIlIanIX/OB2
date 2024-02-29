from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = models.CharField(max_length=30,
                                verbose_name='ник', **NULLABLE)
    number = models.CharField(max_length=13,
                              verbose_name='телефон', unique=True)
    is_subscribed = models.BooleanField(default=False,
                                        verbose_name='есть подписка')

    USERNAME_FIELD = 'number'
    REQUIRED_FIELDS = []
