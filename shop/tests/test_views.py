from django.test import TestCase, Client
from django.urls import reverse

class TestShopViews(TestCase):

    def test_checkout_GET(self):
        client = Client()
        response = client.get(reverse('checkout'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'checkout.html')

    def test_shop_GET(self):
        client = Client()
        response = client.get(reverse('shop'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'shop.html')