from django.test import TestCase

# Create your tests here.
from certificates.models import Assistance, CertificateDoctor

class TestAssistance(TestCase):

    def setUp(self):
        Assistance.objects.create(
            code_capacitation = '9999',
            approved = 'NO',
        )
        self.person = Assistance.objects.get(name='9999')

        self.queryset = Assistance.objects.all()


class TestCertificateDoctor(TestCase):

    def setUp(self):
        CertificateDoctor.objects.create(
            consecutive = '0001',
            date= '2020-01-01',
            diagnostic = 'ALGUN DIAGNOSTICO',
        )
        self.person = CertificateDoctor.objects.get(name='0001')

        self.queryset = CertificateDoctor.objects.all()