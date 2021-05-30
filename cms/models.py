from django.db import models
from ckeditor.fields import RichTextField


class Carrousel(models.Model):
    title = models.CharField(max_length=60)

    def __str__(self):
        return f'{self.title}'


class Image(models.Model):
    alt = models.CharField(max_length=60)
    image = models.FileField(upload_to='cms/images/')
    carrousel = models.ForeignKey(Carrousel, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.alt}'

class Page(models.Model):
    """Model Page"""
    title = models.CharField(
        null=False, blank=False, max_length=50,
        verbose_name="Title",
        help_text="Title")

    slug = models.SlugField(
        null=False, blank=False, max_length=100,
        verbose_name="Slug",
        help_text="Slug")

    class Meta:
        ordering = ["id"]
        verbose_name = "Page"
        verbose_name_plural = "Pages"

    def __str__(self):
        return f'{self.title}'


class Menu(models.Model):
    # template = models.ForeignKey(Template, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(
        max_length=50
    )
    page = models.ForeignKey(Page, on_delete=models.CASCADE, null=True, blank=True)
    description = RichTextField(
        blank=True,
        null=True,
    )
    is_blog = models.BooleanField()

    def __str__(self):
        return f'{self.name}'

class Template(models.Model):
    icon = models.ImageField(
        upload_to='cms/icons',
    )
    logo = models.ImageField(
        upload_to='cms/logos',
    )
    header_title = models.CharField(
        max_length=50
    )
    menu_items = models.ManyToManyField(Menu)
    is_active = models.BooleanField()

    def __str__(self):
        return f'{self.header_title}'

    class Meta:
        verbose_name = 'Template'
        verbose_name_plural = 'Templates'


class Content(models.Model):
    """Model Content"""
    title = models.CharField(
        null=False, blank=False, max_length=50,
        verbose_name="Title",
        help_text="Title")
    page = models.ForeignKey(Page, on_delete=models.CASCADE, null=True)
    carrousel = models.ForeignKey(Carrousel, on_delete=models.SET_NULL, blank=True, null=True)
    body = RichTextField(
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ["id"]
        verbose_name = "Content"
        verbose_name_plural = "Contents"

    def __str__(self):
        return f'{self.title}'


class FooterDescription(models.Model):
    description = RichTextField(
        blank=True,
        null=True,
    )
    template = models.ForeignKey(Template, on_delete=models.SET_NULL, null=True, blank=True)
