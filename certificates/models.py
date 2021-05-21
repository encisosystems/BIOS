from django.db import models

# Create your models here.
class Concept_type(models.Model):
    code = models.AutoField(
        primary_key=True, null=False, 
        blank=False, max_length=15)
    name = models.CharField(
        null=False, blank=False,
        max_length=50)
        
    class Meta:
        ordering=["codigo"]
        verbose_name="Concept_type"
        verbose_name_plural="Concept_type"

    def __str__(self):
        return self.nombre        
        
class Manipulator(models.Model):
    
    birth = models.DateTimeField(
        null=False, blank=False,
        auto_now_add=True)
       
    class Meta:
        verbose_name = 'Manipulator'
        verbose_name_plural = 'Manipulators'

class Company_customer(models.Model):

    nit = models.CharField(
        blank=True, null=True,primary_key=True,
        verbose_name='NIt', max_length=15)
        
    social_reason = models.CharField(
        null=True,blank=True,max_length=30,
        verbose_name='social reason')
        
    phone = models.IntegerField(
        null=True,blank=True,
        max_length=30,verbose_name='Phone Number')
        
    email = models.EmailField(
        blank=True, null=True,
        verbose_name='Email', max_length=30)
        
    adress = models.CharField(
        blank=True,max_length=30,  
        verbose_name='Company address')

    def __str__(self):
        return self.social_reason

    class Meta:
        verbose_name = 'Company Customer'
        verbose_name_plural = 'Company Customers'

class capacity_certificate(models.Model):
    
    consecutive = models.AutoField(
        max_length=30, blank=True, 
        verbose_name='consecutive',
        auto_created=True,primary_key=True)
        
    date = models.DateField(auto_now_add=True)
    
    QR_path = models.URLField(
        max_length=200, verbose_name='QR path', 
        null=True, blank=True)
        
    def str(self):
        return self.QR_path

    class Meta:
        verbose_name = 'capacity certificate'
        verbose_name_plural = 'capacity certificates'