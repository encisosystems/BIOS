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


class Image(TestCase):
    
    def setUp(self):
        Image.objects.create(id=1,title='Main', alt='image 1', image = 'image1.png', carrousel = '1')
        self.image= Image.objects.get(id=1)
        self.queryset = Image.objects.all()

    def test_query_image(self):
        image = self.image.title
        self.assertEqual(image, 'Main')

    def test_update_image(self):
        self.image.title = 'image1 Update'
        self.image.alt = 'image 1 update'
        self.image.alt = 'image1.png'
        self.image.save()
        self.assertEqual(self.image.title, 'image1 Update')

    def test_delete_image(self):
        self.image.delete()
        self.assertNotIn(self.image, self.queryset)