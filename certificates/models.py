from django.db import models

BOOLEAN_CHOICES = (
    ('SI', 'Yes',),
    ('NO', 'No',),
)
class TypeDocument(models.Model):
    name = models.CharField(max_length=100, blank=True, verbose_name='Document Name')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Document Type'
        verbose_name_plural = 'Document Types'

class City(models.Model):
    name = models.CharField(max_length=100, blank=True, verbose_name='City Name')
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

class TypeTest(models.Model):
    code = models.CharField(max_length=100, blank=True, verbose_name='Test Code', null=True)
    name = models.CharField(max_length=100, blank=True, verbose_name='Test Name')
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Test Type'
        verbose_name_plural = 'Test Types'

class Test(models.Model):
    typetest = models.ForeignKey(TypeTest, verbose_name='Choose Test Type', on_delete=models.PROTECT, blank=True, null=True)
    result   = models.CharField(max_length=100, blank=True, verbose_name='Result')
    def __str__(self):
        return self.result
    class Meta:
        verbose_name = 'Test'
        verbose_name_plural = 'Tests'

class ConcepType(models.Model):
    code = models.IntegerField(blank=True, verbose_name='Concept Code', null=True)
    name = models.CharField(max_length=100, blank=True, verbose_name='Concept Name')
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Concept Type'
        verbose_name_plural = 'Concept Types'

class Person(models.Model):
    name           = models.CharField(max_length=100, blank=True, verbose_name='Name', null=True)
    last_name      = models.CharField(max_length=100, blank=True, verbose_name='Last Name', null=True)
    type_document  = models.ForeignKey(TypeDocument, verbose_name='Choose Document Type', on_delete=models.PROTECT, blank=True, null=True)
    identification = models.CharField(max_length=100, blank=True, verbose_name='Identification Number', null=True)
    phone          = models.CharField(max_length=100, blank=True, verbose_name='Phone Number', null=True)
    address        = models.CharField(max_length=250, blank=True, verbose_name='Address')
    job            = models.CharField(max_length=100, blank=True, verbose_name='Job Name', null=True)
    city           = models.ForeignKey(City, verbose_name='Choose City', on_delete=models.PROTECT, blank=True, null=True)
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'Persons'

class Official(models.Model):
    person      = models.ForeignKey(Person, verbose_name='Choose Person', on_delete=models.PROTECT,blank=True, null=True)
    university  = models.CharField(max_length=100, blank=True, verbose_name='University Name')
    specialty   = models.CharField(max_length=100, blank=True, verbose_name='Specialty Name')
    url         = models.URLField(max_length=300, blank=True, verbose_name='Signature Url')

    def __str__(self):
        return self.person.name

    class Meta:
        verbose_name = 'Official'
        verbose_name_plural = 'Officials'

class Doctor(models.Model):
    medical_record = models.CharField(max_length=100, blank=True, verbose_name='Medical Record', null=True)
    resolution     = models.CharField(max_length=100, blank=True, verbose_name='Resolution Number')
    official       = models.ForeignKey(Official, verbose_name='Choose Official', on_delete=models.PROTECT, blank=True, null=True)
    
    def __str__(self):
        return self.rm
    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'

class ClientEntity(models.Model):
    nit           = models.CharField(max_length=100, blank=True, verbose_name='Nit (Tributary Identification Number)', null=True)
    name          = models.CharField(max_length=100, blank=True, verbose_name='Entity Name', null=True)
    business_name = models.CharField(max_length=100, blank=True, verbose_name='Business Name', null=True)
    phone         = models.CharField(max_length=100, blank=True, verbose_name='Phone Number', null=True)
    email         = models.EmailField(max_length=100, blank=True, verbose_name='Email Address', null=True)
    adress        = models.CharField(max_length=100, blank=True, verbose_name='Address')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Client Entity'
        verbose_name_plural = 'Client Entities'

class Manipulator(models.Model):
    person = models.ForeignKey(Person, verbose_name='Choose Person', on_delete=models.PROTECT, blank=True, null=True)
    birth  = models.DateTimeField(auto_now_add=True, verbose_name="Birth Date")
    entity = models.ForeignKey(ClientEntity, verbose_name='Choose Entity', on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.person.name
    class Meta:
        verbose_name = 'Manipulator'
        verbose_name_plural = 'Manipulators'

class Assistance(models.Model):
    assistance        = models.ForeignKey(Manipulator, verbose_name='Choose Manipulator', on_delete=models.PROTECT, blank=True, null=True)
    code_capacitation = models.IntegerField( blank=True, verbose_name='Capacitation Code')
    approved          = models.CharField(max_length=2, choices=BOOLEAN_CHOICES, verbose_name='Approved?', null=True, blank=True)

    def __str__(self):
        return self.assistance.name
    class Meta:
        verbose_name = 'Assistance'
        verbose_name_plural = 'Assistances'

class CertificateAssistance(models.Model):
    assistance  = models.ForeignKey(Assistance, verbose_name='Choose Assistance', on_delete=models.PROTECT, blank=True, null=True)
    consecutive = models.CharField(max_length=30, blank=True, verbose_name='Consecutive')
    date = models.DateField(auto_now_add=True, verbose_name="Certificate Of Assistance Date")
    qr_url = models.URLField(max_length=200, verbose_name='QR Code Url', null=True, blank=True)

    def __str__(self):
        return self.consecutive
    class Meta:
        verbose_name = 'Certificate Assistance'
        verbose_name_plural = 'Certificate Assistances'

class Capacitation(models.Model):
    code = models.ForeignKey(Assistance, verbose_name='Choose Assistance', on_delete=models.PROTECT, blank=True, null=True)
    official = models.ForeignKey(Official, verbose_name='Funcionario', on_delete=models.PROTECT, blank=True, null=True)
    date = models.DateField(auto_now_add=True, verbose_name="Capacitation Date")
    name = models.CharField(max_length=100, blank=True, verbose_name='Capacitacion Name', null=True)
    address = models.CharField(max_length=100, blank=True, verbose_name='Address')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Capacitation'
        verbose_name_plural = 'Capacitations'

class Entity(models.Model):
    nit           = models.CharField(max_length=100, blank=True, verbose_name='Nit (Tributary Identification Number)', null=True)
    name          = models.CharField(max_length=100, blank=True, verbose_name='Entity Name', null=True)
    business_name = models.CharField(max_length=100, blank=True, verbose_name='Business Name', null=True)
    phone         = models.CharField(max_length=100, blank=True, verbose_name='Phone Number', null=True)
    email         = models.EmailField(max_length=100, blank=True, verbose_name='Email Address', null=True)
    address       = models.CharField(max_length=100, blank=True, verbose_name='Address')
    service       = models.CharField(max_length=100, blank=True, verbose_name='Service Description', null=True)
    official      = models.ForeignKey(Official, verbose_name='Choose Official', on_delete=models.PROTECT, blank=True, null=True)
    capacitations = models.ManyToManyField(Capacitation)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Entity'
        verbose_name_plural = 'Entities'
class CapacityCertificate(models.Model):
    consecutive = models.AutoField(blank=True, verbose_name='consecutive', auto_created=True, primary_key=True)
    date = models.DateField(auto_now_add=True, verbose_name='Certificate Generation Date')
    qr_url = models.URLField(max_length=200, verbose_name='Qr Url', null=True, blank=True)

    def str(self):
        return self.qr_url
    class Meta:
        verbose_name = 'Capacity Certificate'
        verbose_name_plural = 'Capacity Certificates'

class CertificateDoctor(models.Model):
    consecutive = models.CharField(max_length=100, verbose_name='Consecutive', blank=True, null=True)
    date        = models.DateField(auto_now_add=True, verbose_name="Certificate Date")
    diagnostic  = models.CharField(max_length=100, verbose_name='Diagnostic', blank=True, null=True)
    result      = models.ForeignKey(Test, verbose_name='Choose Test Result', on_delete=models.PROTECT, blank=True, null=True)
    entity      = models.ForeignKey(Entity, verbose_name='Choose Entity', on_delete=models.PROTECT,blank=True, null=True)
    doctor      = models.ForeignKey(Doctor, verbose_name='Choose Doctor', on_delete=models.PROTECT,blank=True, null=True)
    manipulator = models.ForeignKey(Manipulator, verbose_name='Choose Manipulator', on_delete=models.PROTECT, blank=True, null=True)
    conceptype  = models.ForeignKey(ConcepType, verbose_name='Choose Concep Type', on_delete=models.PROTECT, blank=True, null=True)
    certificateassitance = models.ForeignKey(CertificateAssistance, verbose_name='Choose Certificate Assistance', on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.consecutive
    class Meta:
        verbose_name = 'Doctor Certificate'
        verbose_name_plural = 'Doctor Certificates'
