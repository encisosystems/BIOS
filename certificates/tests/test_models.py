from django.test import TestCase
from certificates.models import *
from django.utils import timezone


# Create your tests here.


class TestPerson(TestCase):

    def setUp(self):
        Person.objects.create(
            name='jorge',
            last_name='cuenca',
            identification='1121943206',
            phone='22323',
            address=' asjasj@gmail.com',
            job='sdsad',
        )
        self.person = Person.objects.get(name='jorge')

        self.queryset = Person.objects.all()

    def test_query_person(self):
        person = self.person.name
        self.assertEqual(person, 'jorge')

    def test_update_order(self):
        self.person.name = 'jorge1'
        self.person.last_name = 'cuenca2'
        self.person.identification = '2323'
        self.person.phone = '232323'
        self.person.adress = 'asdsdsd'
        self.person.job = 'cargo'
        self.person.save()
        self.assertEqual(self.person.name, 'jorge1')

    def test_delete_person(self):
        self.person.delete()
        self.assertNotIn(self.person, self.queryset)


class TestConcepType(TestCase):

    def setUp(self):
        ConcepType.objects.create(
            code='001',
            name='Apto sin restricción',
        )
        self.concept = ConcepType.objects.get(
            name='Apto sin restricción', code='001')

        self.queryset = ConcepType.objects.all()

    def test_query_concept(self):
        concept = self.concept.name
        self.assertEqual(concept, 'Apto sin restricción')

    def test_update_concept(self):
        self.concept.code = '002'
        self.concept.name = 'Apto para trabajar'
        self.concept.save()
        self.assertEqual(self.concept.name, 'Apto para trabajar')

    def test_delete_concept(self):
        self.concept.delete()
        self.assertNotIn(self.concept, self.queryset)


class TestManipulator(TestCase):

    def setUp(self):
        Manipulator.objects.create(
            id=1,
            birth="1992-07-07 01:00:00+00:00",
        )
        self.manipulator = Manipulator.objects.get(id=1)

        self.queryset = Manipulator.objects.all()

    def test_query_manipulator(self):
        manipulator = self.manipulator.id
        self.assertEqual(int(manipulator), 1)

    def test_update_manipulator(self):

        self.manipulator.birth = "1990-07-07 05:00:00+00:00"

        self.manipulator.save()
        self.assertEqual(self.manipulator.birth, "1990-07-07 05:00:00+00:00")

    def test_delete_manipulator(self):
        self.manipulator.delete()
        self.assertNotIn(self.manipulator, self.queryset)


class TestClientEntity(TestCase):

    def setUp(self):
        ClientEntity.objects.create(
            nit='81232323',
            name='Enerca',
            business_name='empresa de energia de casanare',
            phone='3103273109',
            email='contacto@enerca.com.co',
            adress='Marginal de la selva # 6-100',
        )
        self.cliententity = ClientEntity.objects.get(nit='81232323')
        self.queryset = ClientEntity.objects.all()

    def test_query_cliententity(self):
        cliententity = self.cliententity.nit
        self.assertEqual(cliententity, '81232323')

    def test_update_cliententity(self):
        self.cliententity.nit = '87754565'
        self.cliententity.name = 'Enerca'
        self.cliententity.business_name = 'EMPRESA ENERCA'
        self.cliententity.phone = '3234564354'
        self.cliententity.email = 'contacto@enerca.com.co'
        self.cliententity.adress = 'Marginal de la selva KILOMETRO 1 VIA AGUAZUL'
        self.cliententity.save()
        self.assertEqual(self.cliententity.nit, '87754565')

    def test_delete_cliententity(self):
        self.cliententity.delete()
        self.assertNotIn(self.cliententity, self.queryset)


class TestCapacityCertificate(TestCase):

    def setUp(self):
        CapacityCertificate.objects.create(
            consecutive=1,
            date="1992-07-07",
            qr_url="http://localhost:8000/static/img/products/women-3.jpg",
        )
        self.capacitycertificate = CapacityCertificate.objects.get(
            consecutive=1)
        self.queryset = CapacityCertificate.objects.all()

    def test_query_capacitycertificate(self):
        capacitycertificate = self.capacitycertificate.consecutive
        self.assertEqual(int(capacitycertificate), 1)

    def test_update_capacitycertificate(self):
        self.capacitycertificate.consecutive = 3
        self.capacitycertificate.date = "1992-07-07"
        self.capacitycertificate.qr_url = "http://localhost:8000/static/img/products/women-2.jpg"
        self.capacitycertificate.save()
        self.assertEqual(self.capacitycertificate.consecutive, 3)

    def test_delete_capacitycertificate(self):
        self.capacitycertificate.delete()
        self.assertNotIn(self.capacitycertificate, self.queryset)
