from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):

    def test_blog_GET(self):
        client = Client()
        response = client.get(reverse('blog'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'blog.html')

    def test_blog_details_GET(self):
        client = Client()
        response = client.get(reverse('blog-details'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'blog-details.html')