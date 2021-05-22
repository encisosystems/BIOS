from django.db import models

# Create your models here.
class TypeOfExam(models.Model):
    code = models.CharField(max_length=30, blank=True, verbose_name='Codigo', null=True)
    name = models.CharField(max_length=30, blank=True, verbose_name='Nombre', null=True)


class MedicalCertificate(models.Model):
    consecutive = models.CharField()
    generation_date = models.DateField()
    url_qr = models.CharField(max_length=30, blank=True, verbose_name='Url Code QR')
    doctor = models.BigIntegerField()
    bussines = models.BigIntegerField()
    diagnostic = models.CharField(max_length=300, verbose_name="Diagnostico")
    manipulator = models.CharField()
    concept = models.CharField()

class AttendanceCertificate(models.Model):
    consecutive = models.CharField()
    generation_date = models.DateField()
    url_qr = models.CharField(max_length=30, blank=True, verbose_name='Url Code QR')

class Assistance(models.Model):
    capacitation_code = models.BigIntegerField()
    assistance = models.BigIntegerField()
    aproved_status = models.BooleanField()

class result(models.Model):
    type_of_exam = models.BigIntegerField()
    result = models.CharField()


