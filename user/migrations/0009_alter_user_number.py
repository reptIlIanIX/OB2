# Generated by Django 4.2.4 on 2024-02-21 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_user_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='number',
            field=models.CharField(max_length=15, unique=True, verbose_name='телефон'),
        ),
    ]