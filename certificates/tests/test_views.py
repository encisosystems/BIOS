from certificates.models import CertificateAssistance
from django.test import TestCase, Client
from django.urls import reverse
import datetime

class TestViews(TestCase):
    def setUp(self):
         CertificateAssistance.objects.create(
             consecutive="001", 
             qr_url="",
             certificate_date=datetime.datetime(2020, 5, 17)
            )
            
    def test_principal_lists_GET(self):
        client = Client()
        response = client.get(reverse('manipulator'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'manipulator.html')

    def test_certificate_letter_GET(self):
        client = Client()
        response = client.get(reverse('certificate-letter',kwargs={'pk': 1}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'certificate-letter.html')