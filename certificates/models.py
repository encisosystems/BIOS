from django.db import models

# Create your models here.

class Concept_type(models.Model):
    code = models.AutoField(
        primary_key=True, null=False, 
        blank=False)
    name = models.CharField(
        null=False, blank=False,
        max_length=50)
        
    class Meta:
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
        blank=True, primary_key=True,
        verbose_name='NIt', max_length=15)
        
    social_reason = models.CharField(
        null=True,blank=True,max_length=30,
        verbose_name='social reason')
        
    phone = models.IntegerField(
        null=True,blank=True,
        verbose_name='Phone Number')
        
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
        blank=True, 
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
        
class TypeOfExam(models.Model):
    code = models.CharField(max_length=30, blank=True, verbose_name='Codigo', null=True)
    name = models.CharField(max_length=30, blank=True, verbose_name='Nombre', null=True)


class MedicalCertificate(models.Model):
    consecutive = models.CharField(max_length=30, blank=True,)
    generation_date = models.DateField()
    url_qr = models.CharField(max_length=30, blank=True, verbose_name='Url Code QR')
    doctor = models.BigIntegerField()
    bussines = models.BigIntegerField()
    diagnostic = models.CharField(max_length=300, verbose_name="Diagnostico")
    manipulator = models.CharField(max_length=60, blank=True,)
    concept = models.CharField(max_length=60, blank=True,)

class AttendanceCertificate(models.Model):
    consecutive = models.CharField(max_length=30, blank=True,)
    generation_date = models.DateField()
    url_qr = models.CharField(max_length=30, blank=True, verbose_name='Url Code QR')

class Assistance(models.Model):
    capacitation_code = models.BigIntegerField()
    assistance = models.BigIntegerField()
    aproved_status = models.BooleanField()

class result(models.Model):
    type_of_exam = models.BigIntegerField()
    result = models.CharField(max_length=60, blank=True,)