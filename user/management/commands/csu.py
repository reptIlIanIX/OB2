from django.core.management import BaseCommand

from user.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(number='+79150838576', name='Denis', is_staff=True, is_superuser=True)
        user.set_password('123qwe456rty')
        user.save()
