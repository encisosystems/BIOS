from django.test import TestCase
from cms.models import *

# Create your tests here.


class TestCarrousel(TestCase):
    
    def setUp(self):
        Carrousel.objects.create(id=1,title='Main')
        self.carrousel= Carrousel.objects.get(id=1)
        self.queryset = Carrousel.objects.all()

    def test_query_carrousel(self):
        carrousel= self.carrousel.title
        self.assertEqual(carrousel, 'Main')

    def test_update_carrousel(self):
        self.carrousel.title = 'One'
        self.carrousel.save()
        self.assertEqual(self.carrousel.title, 'One')

    def test_delete_carrousel(self):
        self.carrousel.delete()
        self.assertNotIn(self.carrousel, self.queryset)


class TestImage(TestCase):

    def setUp(self):
        Image.objects.create(id=1, alt='600')
        self.image = Image.objects.get(id=1)
        self.queryset = Image.objects.all()
    
    def test_query_image(self):
        image = self.image.alt
        self.assertEqual(image, '600')
    
    def test_update_image(self):
        self.image.alt = '700'
        self.image.save()
        self.assertEqual(self.image.alt, '700')

    def test_delete_image(self):
        self.image.delete()
        self.assertNotIn(self.image, self.queryset)

    
class TestTemplate(TestCase):
    
    def setUp(self):
        Template.objects.create(id=1, icon="icon.icon",logo="logo.png",is_active=True, header_title='Index')
        self.template = Template.objects.get(id=1)
        self.queryset = Template.objects.all()

    def test_query_template(self):
        template = self.template.header_title
        self.assertEqual(template, 'Index')

    def test_update_template(self):
        self.template.header_title = 'MainTemplate'
        self.template.save()
        self.assertEqual(self.template.header_title, 'MainTemplate')

    def test_delete_template(self):
        self.template.delete()
        self.assertNotIn(self.template, self.queryset)
