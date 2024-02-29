from django.test import TestCase
from django.urls import reverse

from blog.models import Blog


class TestBlog(TestCase):
    @classmethod
    def setUpTestData(cls):
        Blog.objects.create(name='Big',
                            description='Very good description')
        Blog.objects.create(name='Small',
                            description='Not so good description')

    def test_description(self):
        big = Blog.objects.get(name="Big")
        small = Blog.objects.get(name="Small")
        self.assertEqual(big.description, 'Very good description')
        self.assertEqual(small.description, 'Not so good description')

    def test_name_label(self):
        blog = Blog.objects.get(id=1)
        field_label = blog._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'название')

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/blog/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('blog:list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('blog:list'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'OB2/blog_list.html')
