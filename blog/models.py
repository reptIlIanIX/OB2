from django.db import models

from OB2 import settings
from user.models import User

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    name = models.CharField(max_length=15, verbose_name='название')
    description = models.TextField(max_length=50, verbose_name='описание')
    image = models.ImageField(upload_to='blog/', verbose_name='картинка', **NULLABLE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='владелец')

    def __str__(self):
        return f'{self.name} - {self.description}'

    class Meta:
        verbose_name = 'блог'
