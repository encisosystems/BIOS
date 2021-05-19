from django.db import models

# Create your models here.

class footer(models.Model):
    company = models.CharField(max_length=30)
    year = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    mail = models.CharField(max_length=30)


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
