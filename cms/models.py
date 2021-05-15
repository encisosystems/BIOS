from django.db import models

# Create your models here.

class footer(models.Model):
company = models.CharField(max_length=30)
year = models.CharField(max_length=30)
phone = models.CharField(max_length=30)
mail = models.CharField(max_length=30)
