from django.test import TestCase

# Create your tests here.
from certificates.models import Person, Entity, Official, Doctor, Capacitation


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

    def test_update_person(self):
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


class TestEntity(TestCase):

    def setUp(self):
        Entity.objects.create(
            nit='jorge',
            name='cuenca',
            business_name='1121943206',
            phone='22323',
            email=' asjasj@gmail.com',
            address='sdsad',
            service='22323',
        )
        self.Entity = Entity.objects.get(name='cuenca')
        self.queryset = Entity.objects.all()

    def test_query_entity(self):
        Entity = self.Entity.name
        self.assertEqual(Entity, 'cuenca')

    def test_update_entity(self):
        self.Entity.nit = 'jorge1'
        self.Entity.name = 'cuenca2'
        self.Entity.business_name = '2323'
        self.Entity.phone = '232323'
        self.Entity.email = 'asdsdsd'
        self.Entity.adress = 'asdsdsd'
        self.Entity.service = 'cargo'
        self.Entity.save()
        self.assertEqual(self.Entity.name, 'cuenca2')

    def test_delete_entity(self):
        self.Entity.delete()
        self.assertNotIn(self.Entity, self.queryset)


class TestOfficial(TestCase):

    def setUp(self):
        Official.objects.create(
            university='Unillanos',
            specialty='microbiologo',
            url='http://firma.com/sdsad',

        )
        self.official = Official.objects.get(specialty='microbiologo')

        self.queryset = Official.objects.all()


    def test_query_official(self):
        official = self.official.specialty
        self.assertEqual(official, 'microbiologo')


    def test_update_official(self):
        self.official.university = 'unillanos1'
        self.official.specialty = 'doctor'
        self.official.url = 'https://ssadsad.com/sdsd'
        self.official.save()
        self.assertEqual(self.official.specialty, 'doctor')


    def test_delete_official(self):
        self.official.delete()
        self.assertNotIn(self.official, self.queryset)


class TestDoctor(TestCase):

    def setUp(self):
        Doctor.objects.create(
            medical_record='prueba',
            resolution='45435',

        )
        self.doctor = Doctor.objects.get(medical_record='prueba')

        self.queryset = Doctor.objects.all()


    def test_query_doctor(self):
        doctor = self.doctor.medical_record
        self.assertEqual(doctor, 'prueba')


    def test_update_doctor(self):
        self.doctor.medical_record = 'prueba1'
        self.doctor.resolution = '123123'
        self.doctor.save()
        self.assertEqual(self.doctor.medical_record, 'prueba1')


    def test_delete_doctor(self):
        self.doctor.delete()
        self.assertNotIn(self.doctor, self.queryset)


class TestCapacitation(TestCase):

    def setUp(self):
        Capacitation.objects.create(
            name='capacitation',
            address=' asjasj@gmail.com',

        )
        self.capacitation = Capacitation.objects.get(name='capacitation')

        self.queryset = Capacitation.objects.all()


    def test_query_capacitation(self):
        capacitation = self.capacitation.name
        self.assertEqual(capacitation, 'capacitation')


    def test_update_capacitation(self):
        self.capacitation.name = 'capacitation1'
        self.capacitation.adress = 'asdsdsd'
        self.capacitation.save()
        self.assertEqual(self.capacitation.name, 'capacitation1')


    def test_delete_capacitation(self):
        self.capacitation.delete()
        self.assertNotIn(self.capacitation, self.queryset)
