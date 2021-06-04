from certificates.models import CapacityCertificate, CertificateAssistance, CertificateDoctor, ConcepType, Test
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
        CertificateDoctor.objects.create(
            consecutive="001",
            diagnostic="Aprobado"
        )
        Test.objects.create(
            result="Aprobado",
            certificate=CertificateDoctor.objects.first()
        )
        ConcepType.objects.create(
            name="Prueba",
            code="001"
        )

        CapacityCertificate.objects.create(
            consecutive='1',
            date=datetime.datetime(2020, 5, 29),
            qr_url="wwwpruebascom"
        )

    def test_principal_lists_GET(self):
        client = Client()
        response = client.get(reverse('manipulator'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'manipulator.html')

    def test_certificate_letter_GET(self):
        client = Client()
        response = client.get(reverse('certificate-letter', kwargs={'pk': 1}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'certificate-letter.html')

    def test_certificate_medical_GET(self):
        client = Client()
        # I need the recenty inserted ID
        element = CertificateDoctor.objects.first()
        response = client.get(
            reverse('medical-certificate', kwargs={'certificate_id': element.id}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'medical-certificate.html')

    def test_cma_carnet_GET(self):
        client = Client()
        response = client.get(reverse('cma-carnet', kwargs={'pk': 1}))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cma-carnet.html')
