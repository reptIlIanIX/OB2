from django.test import TestCase
from django.urls import reverse

from user.models import User


class TestUser(TestCase):

    # Create your tests here.
    def setUp(self):
        # Создание двух пользователей
        test_user1 = User.objects.create_user(username="gud", number='+79160889808', password='12345')
        test_user1.save()
        test_user2 = User.objects.create_user(username="bad", number='+79160889878', password='654321')
        test_user2.save()

    def test_redirect_if_not_logged_in(self):
        resp = self.client.get('/blog/edit/5/')
        self.assertRedirects(resp, '/denied/?next=/blog/edit/5/')
    #
    # def test_logged_in_uses_correct_template(self):
    #     login = self.client.login(number='79160889808', password='12345')
    #     resp = self.client.get(reverse('blog:detail'))
    #
    #     # Проверка что пользователь залогинился
    #     self.assertEqual(str(resp.context['user']), '79160889808')
    #     # Проверка ответа на запрос
    #     self.assertEqual(resp.status_code, 200)
    #     # Проверка того, что мы используем правильный шаблон
    #
    #     self.assertTemplateUsed(resp, 'catalog/bookinstance_list_borrowed_user.html')
