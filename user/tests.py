from django.test import TestCase
from django.urls import reverse

from user.models import User


class TestUser(TestCase):

    # Create your tests here.
    def setUp(self):
        # Создание двух пользователей
        self.user = User.objects.create(
            number='+79160889803',
            is_active=True
        )
        self.user.set_password('12345678')
        self.user.save()

    def test_redirect_if_not_logged_in(self):
        resp = self.client.get('/blog/edit/5/')
        self.assertRedirects(resp, '/denied/?next=/blog/edit/5/')

    def test_logged_in_uses_correct_template(self):
        # self.assertTrue(force_login)
        resp = self.client.get(reverse('user:login'))

        # Проверка что пользователь залогинился
        # self.assertEqual(str(resp.context['user']), '79160889803')
        # # Проверка ответа на запрос
        self.assertEqual(resp.status_code, 200)
        # # Проверка того, что мы используем правильный шаблон
        #
        self.assertTemplateUsed(resp, "OB2/login.html")
