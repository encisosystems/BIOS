from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def test_blog_GET(self):
        client = Client()
        response = client.get(reverse('blog'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'blog.html')

