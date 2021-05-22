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
        verbose_name = 'Type Document'
        verbose_name_plural = 'Type Documents'

class City(models.Model):
    name = models.CharField(max_length=30, blank=True, verbose_name='Nombre de ciudad')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

class TypeTest(models.Model):
    code = models.IntegerField(blank=True, verbose_name='codigo', null=True)
    name = models.CharField(max_length=30, blank=True, verbose_name='Tipo de examen')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Tipo Test'
        verbose_name_plural = 'Type Tests'

class Test(models.Model):
    typetest = models.ForeignKey(TypeTest, verbose_name='TIpo de  examen', on_delete=models.PROTECT,
                                      blank=True, null=True)
    result = models.CharField(max_length=30, blank=True, verbose_name='Resultado')
    def __str__(self):
        return self.result
    class Meta:
        verbose_name = 'Test'
        verbose_name_plural = 'Tests'

class ConcepType(models.Model):
    code = models.IntegerField(blank=True, verbose_name='codigo', null=True)
    name = models.CharField(max_length=30, blank=True, verbose_name='Tipo de concepto')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Type Concept'
        verbose_name_plural = 'Type Concepts'

class Person(models.Model):
    name = models.CharField(max_length=30, blank=True, verbose_name='NOmbres', null=True)
    last_name = models.CharField(max_length=30, blank=True, verbose_name='Apellidos', null=True)
    phone = models.IntegerField(blank=True, verbose_name='telefono', null=True)
    type_document = models.ForeignKey(TypeDocument, verbose_name='TIpode documento', on_delete=models.PROTECT,
                                      blank=True, null=True)
    identification = models.IntegerField(verbose_name='Número de identificación', blank=True, null=True)
    address = models.CharField(max_length=30, blank=True, verbose_name='Direccion')
    city = models.ForeignKey(City, verbose_name='Ciudad', on_delete=models.PROTECT,
                                      blank=True, null=True)
    job = models.CharField(max_length=30, blank=True, verbose_name='Cargo', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'

class Official(models.Model):
    person = models.ForeignKey(Person, verbose_name='Persona', on_delete=models.PROTECT,blank=True, null=True)
    university = models.CharField(max_length=30, blank=True, verbose_name='Universidad')
    especiality= models.CharField(max_length=30, blank=True, verbose_name='Especialidad')
    url = models.URLField(max_length=30, blank=True, verbose_name='Ruta firma')

    def __str__(self):
        return self.person.name

    class Meta:
        verbose_name = 'Official'
        verbose_name_plural = 'Officials'

class Doctor(models.Model):
    rm = models.CharField(max_length=30, blank=True, verbose_name='RM', null=True)
    resolution = models.CharField(max_length=30, blank=True, verbose_name='Resolucion')
    official = models.ForeignKey(Official, verbose_name='Funcionario', on_delete=models.PROTECT,
                               blank=True, null=True)
    def __str__(self):
        return self.rm

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'

class ClientEntity(models.Model):
    nit = models.CharField(verbose_name='NIt', max_length=10, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, verbose_name='Nombre de la empresa', null=True)
    business_name = models.CharField(verbose_name='Razon Social', max_length=50, blank=True, null=True)
    phone = models.IntegerField(blank=True, verbose_name='telefono', null=True)
    email = models.EmailField(verbose_name='Email', max_length=10, blank=True, null=True)
    adress = models.CharField(max_length=30, blank=True, verbose_name='Direccion')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Client Entity'
        verbose_name_plural = 'Client Entities'

class Manipulator(models.Model):
    person = models.ForeignKey(Person, verbose_name='Persona', on_delete=models.PROTECT,
                                      blank=True, null=True)
    birth = models.DateTimeField(auto_now_add=True)
    entity = models.ForeignKey(ClientEntity, verbose_name='Empresa de cliente', on_delete=models.PROTECT,
                                      blank=True, null=True)

    def __str__(self):
        return self.person.name

    class Meta:
        verbose_name = 'Manipulator'
        verbose_name_plural = 'Manipulators'

class Assistance(models.Model):
    assistance = models.ForeignKey(Manipulator, verbose_name='Asistente', on_delete=models.PROTECT,
                               blank=True, null=True)
    code_capacitation = models.IntegerField( blank=True, verbose_name='Codigo de capacitacion')
    approved = models.CharField(max_length=2, choices=BOOLEAN_CHOICES, verbose_name='Esta aprobado?', null=True, blank=True)

    def __str__(self):
        return self.assistance.name

    class Meta:
        verbose_name = 'Assistance'
        verbose_name_plural = 'Assistances'

class CertificateAssistance(models.Model):
    assistance = models.ForeignKey(Assistance, verbose_name='Asistencia', on_delete=models.PROTECT,
                               blank=True, null=True)
    consecutive = models.CharField(max_length=30, blank=True, verbose_name='Consecutivo')
    date = models.DateField(auto_now_add=True)
    qr_url = models.URLField(max_length=200, verbose_name='Ruta qr', null=True, blank=True)

    def __str__(self):
        return self.consecutive

    class Meta:
        verbose_name = 'Certificate Assistance'
        verbose_name_plural = 'Certificate Assistances'

class Capacitation(models.Model):
    code = models.ForeignKey(Assistance, verbose_name='Codigo', on_delete=models.PROTECT,
                               blank=True, null=True)
    official = models.ForeignKey(Official, verbose_name='Funcionario', on_delete=models.PROTECT,
                                 blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=30, blank=True, verbose_name='Nombre capacitacion', null=True)
    address = models.CharField(max_length=30, blank=True, verbose_name='Direccion')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Capacitation'
        verbose_name_plural = 'Capacitations'

class Entity(models.Model):
    nit = models.CharField(verbose_name='NIt', max_length=10, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, verbose_name='Nombre de la empresa', null=True)
    business_name = models.CharField(verbose_name='Razon Social', max_length=50, blank=True, null=True)
    phone = models.IntegerField(blank=True, verbose_name='telefono', null=True)
    email = models.EmailField(verbose_name='Email', max_length=10, blank=True, null=True)
    address = models.CharField(max_length=30, blank=True, verbose_name='Direccion')
    service = models.CharField(verbose_name='Descripcion de servicio', max_length=50, blank=True, null=True)
    official = models.ForeignKey(Official, verbose_name='Funcionario', on_delete=models.PROTECT,
                               blank=True, null=True)
    capacitations = models.ManyToManyField(Capacitation)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Entity'
        verbose_name_plural = 'Entities'


class CapacityCertificate(models.Model):
    consecutive = models.AutoField(
        blank=True,
        verbose_name='consecutive',
        auto_created=True, primary_key=True)

    date = models.DateField(auto_now_add=True,
                            verbose_name='Generation date certificate')

    QR_path = models.URLField(
        max_length=200, verbose_name='QR path',
        null=True, blank=True)

    def str(self):
        return self.QRpath

    class Meta:
        verbose_name = 'Capacity Certificate'
        verbose_name_plural = 'Capacity Certificates'

class CertificateDoctor(models.Model):
    consecutive = models.CharField(verbose_name='Consecutivo', max_length=10, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    result = models.ForeignKey(Test, verbose_name='Resultado', on_delete=models.PROTECT,
                               blank=True, null=True)
    diagnostic = models.CharField(max_length=30, blank=True, verbose_name='Diagnostico', null=True)
    entity = models.ForeignKey(Entity, verbose_name='Empresa', on_delete=models.PROTECT,
                               blank=True, null=True)
    doctor = models.ForeignKey(Doctor, verbose_name='Doctor', on_delete=models.PROTECT,
                               blank=True, null=True)
    manipulator = models.ForeignKey(Manipulator, verbose_name='Manipulador', on_delete=models.PROTECT,
                               blank=True, null=True)
    conceptype = models.ForeignKey(ConcepType, verbose_name='Tipo de concepto', on_delete=models.PROTECT,
                               blank=True, null=True)
    certificateassitance = models.ForeignKey(CertificateAssistance, verbose_name='Tipo de concepto', on_delete=models.PROTECT,
                                   blank=True, null=True)

    def __str__(self):
        return self.consecutive

    class Meta:
        verbose_name = 'Doctor Certificate'
        verbose_name_plural = 'Doctor Certificates'
