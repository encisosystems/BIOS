from django.db import models
BOOLEAN_CHOICES = (
        ('SI', 'SI',),
        ('NO', 'NO',),
    )
class TypeDocument(models.Model):
    name = models.CharField(max_length=30, blank=True, verbose_name='Tipo de documento')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Tipo de documento'
        verbose_name_plural = 'TIpo de documentos'
class City(models.Model):
    name = models.CharField(max_length=30, blank=True, verbose_name='Nombre de ciudad')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Sectores'
class Typetest(models.Model):
    code = models.IntegerField(max_length=30, blank=True, verbose_name='codigo', null=True)
    name = models.CharField(max_length=30, blank=True, verbose_name='Tipo de examen')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Tipo de prueba'
        verbose_name_plural = 'Tipo de prueba'


class Person(models.Model):
    name = models.CharField(max_length=30, blank=True, verbose_name='NOmbres', null=True)
    last_name = models.CharField(max_length=30, blank=True, verbose_name='Apellidos', null=True)
    phone = models.IntegerField(max_length=30, blank=True, verbose_name='telefono', null=True)
    type_document = models.ForeignKey(TypeDocument, verbose_name='TIpode documento', on_delete=models.PROTECT,
                                      blank=True, null=True)
    identification = models.IntegerField(max_length=30, verbose_name='Número de identificación', blank=True, null=True)
    adress = models.CharField(max_length=30, blank=True, verbose_name='Direccion')
    city = models.ForeignKey(City, verbose_name='Ciudad', on_delete=models.PROTECT,
                                      blank=True, null=True)
    job = models.CharField(max_length=30, blank=True, verbose_name='Cargo', null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
class Official(models.Model):
    person = models.ForeignKey(TypeDocument, verbose_name='Persona', on_delete=models.PROTECT,blank=True, null=True)
    university = models.CharField(max_length=30, blank=True, verbose_name='Universidad')
    especialidad = models.CharField(max_length=30, blank=True, verbose_name='Especialidad')
    url = models.URLField(max_length=30, blank=True, verbose_name='Ruta firma')
    def __str__(self):
        return self.person.name
    class Meta:
        verbose_name = 'FUncionario'
        verbose_name_plural = 'Funcionarios'
class Doctor(models.Model):
    rm = models.CharField(max_length=30, blank=True, verbose_name='RM', null=True)
    resolution = models.CharField(max_length=30, blank=True, verbose_name='Resolucion')
    official = models.ForeignKey(Official, verbose_name='FUncionario', on_delete=models.PROTECT,
                               blank=True, null=True)
    def __str__(self):
        return self.rm
    class Meta:
        verbose_name = 'Medico'
        verbose_name_plural = 'Medicos'
class ClientEntity(models.Model):
    nit = models.CharField(verbose_name='NIt', max_length=10, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, verbose_name='Nombre de la empresa', null=True)
    business_name = models.CharField(verbose_name='Razon Social', max_length=50, blank=True, null=True)
    phone = models.IntegerField(max_length=30, blank=True, verbose_name='telefono', null=True)
    email = models.EmailField(verbose_name='Email', max_length=10, blank=True, null=True)
    adress = models.CharField(max_length=30, blank=True, verbose_name='Direccion')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Empresa de clientee'
        verbose_name_plural = 'Empresas de clientes'

class Capacitation(models.Model):
    code = models.ForeignKey(Assistance, verbose_name='Codigo', on_delete=models.PROTECT,
                               blank=True, null=True)
    official = models.ForeignKey(Official, verbose_name='Funcionario', on_delete=models.PROTECT,
                                 blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=30, blank=True, verbose_name='Nombre capacitacion', null=True)
    adress = models.CharField(max_length=30, blank=True, verbose_name='Direccion')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Asistencia'
        verbose_name_plural = 'Asistencias'
class Entity(models.Model):
    nit = models.CharField(verbose_name='NIt', max_length=10, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, verbose_name='Nombre de la empresa', null=True)
    business_name = models.CharField(verbose_name='Razon Social', max_length=50, blank=True, null=True)
    phone = models.IntegerField(max_length=30, blank=True, verbose_name='telefono', null=True)
    email = models.EmailField(verbose_name='Email', max_length=10, blank=True, null=True)
    adress = models.CharField(max_length=30, blank=True, verbose_name='Direccion')
    service = models.CharField(verbose_name='Descripcion de servicio', max_length=50, blank=True, null=True)
    official = models.ForeignKey(Official, verbose_name='Funcionario', on_delete=models.PROTECT,
                               blank=True, null=True)
    capacitations = models.ManyToManyField(Capacitation)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'



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

