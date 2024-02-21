from django.db import models

from user.models import User

NULLABLE = {'blank': True, 'null': True}


class Blog(models.Model):
    name = models.CharField(max_length=15, verbose_name='название')
    description = models.TextField(max_length=50, verbose_name='описание')
    image = models.ImageField(upload_to='blog/', verbose_name='картинка', **NULLABLE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.name} - {self.description}'

    class Meta:
        verbose_name = 'блог'
