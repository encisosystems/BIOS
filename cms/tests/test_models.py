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

