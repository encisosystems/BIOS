from django.test import TestCase
from cms.models import *


# Create your tests here.

class TestCarrousel(TestCase):

    def setUp(self):
        Carrousel.objects.create(id=1, title='Main')
        self.carrousel = Carrousel.objects.get(id=1)
        self.queryset = Carrousel.objects.all()

    def test_query_carrousel(self):
        carrousel = self.carrousel.title
        self.assertEqual(carrousel, 'Main')

    def test_update_carrousel(self):
        self.carrousel.title = 'One'
        self.carrousel.save()
        self.assertEqual(self.carrousel.title, 'One')

    def test_delete_carrousel(self):
        self.carrousel.delete()
        self.assertNotIn(self.carrousel, self.queryset)


class TestPage(TestCase):

    def setUp(self):
        Page.objects.create(id=1, title='One', slug='/hello')
        self.page = Page.objects.get(id=1)
        self.queryset = Page.objects.all()

    def test_query_carrousel(self):
        title = self.page.title
        slug = self.page.slug
        self.assertEqual(title, 'One')
        self.assertEqual(slug, '/hello')

    def test_update_carrousel(self):
        self.page.title = 'Two'
        self.page.save()
        self.assertEqual(self.page.title, 'Two')

    def test_delete_carrousel(self):
        self.page.delete()
        self.assertNotIn(self.page, self.queryset)


class TestContent(TestCase):

    def setUp(self):
        Content.objects.create(id=1, title='One', body='hello')
        self.content = Content.objects.get(id=1)
        self.queryset = Content.objects.all()

    def test_query_carrousel(self):
        title = self.content.title
        body = self.content.body
        self.assertEqual(title, 'One')
        self.assertEqual(body, 'hello')

    def test_update_carrousel(self):
        self.content.title = 'Two'
        self.content.save()
        self.assertEqual(self.content.title, 'Two')

    def test_delete_carrousel(self):
        self.content.delete()
        self.assertNotIn(self.content, self.queryset)


class TestImage(TestCase):

    def setUp(self):
        Image.objects.create(id=1, alt='image 1', image='image1.png')
        self.image = Image.objects.get(id=1)
        self.queryset = Image.objects.all()

    def test_query_image(self):
        image = self.image.alt
        self.assertEqual(image, 'image 1')

    def test_update_image(self):
        self.image.alt = 'image 1 Update'
        self.image.save()
        self.assertEqual(self.image.alt, 'image 1 Update')

    def test_delete_image(self):
        self.image.delete()
        self.assertNotIn(self.image, self.queryset)


class TestFooterDescription(TestCase):

    def setUp(self):
        FooterDescription.objects.create(id=1, description='Contacto')
        self.footerdescription = FooterDescription.objects.get(id=1)
        self.queryset = FooterDescription.objects.all()

    def test_query_footerdescription(self):
        footerdescription = self.footerdescription.description
        self.assertEqual(footerdescription, 'Contacto')

    def test_update_footerdescription(self):
        self.footerdescription.description = 'Curso'
        self.footerdescription.save()
        self.assertEqual(self.footerdescription.description, 'Curso')

    def test_delete_footerdescription(self):
        self.footerdescription.delete()
        self.assertNotIn(self.footerdescription, self.queryset)


class TestMenu(TestCase):

    def setUp(self):
        Menu.objects.create(id=1, name='Servicios')
        self.menu = Menu.objects.get(id=1)
        self.queryset = Menu.objects.all()

    def test_query_menu(self):
        menu = self.menu.name
        self.assertEqual(menu, 'Servicios')

    def test_update_menu(self):
        self.menu.name = 'Contacto'
        self.menu.save()
        self.assertEqual(self.menu.name, 'Contacto')

    def test_delete_menu(self):
        self.menu.delete()
        self.assertNotIn(self.menu, self.queryset)


class TestTemplate(TestCase):

    def setUp(self):
        Template.objects.create(id=1, is_active=True, header_title='Index')
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
