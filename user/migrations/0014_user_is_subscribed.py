# Generated by Django 4.2.4 on 2024-03-03 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_subscribed',
            field=models.BooleanField(default=False, verbose_name='есть подписка'),
        ),
    ]
