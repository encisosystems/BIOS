from django.db import models

# Create your models here.

class FooterDescription(models.Model):
    description = models.TextField(
        max_length=200,
        blank = True,
        null = True
    )
    type_desc = models.CharField(
        max_length=60,
        blank = True,
        null = True
    )
    value = models.CharField(
        max_length=60,
        blank = True,
        null = True
    )

class Menu(models.Model):
    page= models.CharField(max_length=60)

class Carrousel(models.Model):
    title = models.CharField(max_length=60)    

class Image(models.Model):
    title = models.CharField(max_length=60)
    alt = models.CharField(max_length=60)
    image = models.FileField(upload_to='images/')

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

    class Meta:
        ordering = ["id"]
        verbose_name = "Content"
        verbose_name_plural = "Contents"

class Page(models.Model):
    """Model Page"""
    title = models.CharField(
        null=False, blank=False, max_length=50,
        verbose_name="Title",
        help_text="Title")
    slug = models.CharField(
        null=False, blank=False, max_length=100,
        verbose_name="Slug",
        help_text="Slug")

    class Meta:
        ordering = ["id"]
        verbose_name = "Page"
        verbose_name_plural = "Pages"
