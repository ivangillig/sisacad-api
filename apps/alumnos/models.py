from curses import meta
from operator import methodcaller
from django.db import models
from django.conf import settings
from apps.users.models import Person
from apps.base.models import BaseModel

# Create your models here.
class Student(Person):
    
    family_phone = models.CharField('Teléfono familiar', max_length=15, blank=True, null=True)
    medical_treatment = models.BooleanField('Tratamiento médico', default=False, blank=True, null=True)
    medications = models.TextField('Medicamentos', max_length=200, blank=True, null=True)
    allergies = models.TextField('Alergias', max_length=200, blank=True, null=True)
    observations = models.TextField('Observaciones', max_length=200, blank=True, null=True)
    school_cert_destinty = models.CharField('Destino de certificado escolar', max_length=30, blank=True, null=True)
    admission_date = models.DateField('Fecha de ingreso', auto_now=False, auto_now_add=False, blank=True, null=True)
    leaving_date = models.DateField('Fecha de egreso', auto_now=False, auto_now_add=False, blank=True, null=True)
    trips_auth = models.BooleanField('Autorización de paseos', default=False)
    medical_auth = models.BooleanField('Autorización médica', default=False)
    leave_auth = models.BooleanField('Autorización de salida', default=False)
    public_auth = models.BooleanField('Autorización para publicar', default=False)

    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'

    def __str__(self):
        text = '{} {}'.format(
            self.first_lastname,
            self.first_name,
        )
        return text

class Tutor(Person):

    profession = models.CharField('Profesión', max_length=15, blank=True, null=True)
    job_address = models.CharField('Domicilio laboral', max_length=30, blank=True, null=True)
    job_phone = models.CharField('Teléfono laboral', max_length=12, blank=True, null=True)

    class Meta:
        verbose_name = 'Tutor'
        verbose_name_plural = 'Tutores'

    def __str__(self):
        text = '{} {}'.format(
            self.first_name,
            self.first_lastname,
        )
        return text

class Student_Tutor(BaseModel):

    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Alumno')
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)

    RELATIONSHIP_CHOICES = [
        ('Madre', 'Madre'),
        ('Padre', 'Padre'),
        ('Tutor legal', 'Tutor legal'),
    ]
    relationship = models.CharField(
        'Vínculo',
        max_length=15,
        choices = RELATIONSHIP_CHOICES,
        default='Tutor legal',
        )
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['tutor', 'student'], name='tutor_student_combination'
            )
        ]
        verbose_name = 'Alumno_Tutor'
        verbose_name_plural = 'Alumnos_Tutores'

    def __str__(self):
        text = '{}'.format(
            self.relationship,
        )
        return text

class Withdraw_Authorized(BaseModel):

    doc_number = models.CharField('DNI', max_length=15, primary_key=True, unique=True)
    name = models.CharField('Nombre', max_length=15, blank=True, null=True)
    lastname = models.CharField('Apellido', max_length=15, blank=True, null=True)
    phone = models.CharField('Teléfono', max_length=15, blank=True, null=True)

    class Meta:
        verbose_name = 'Autorizado'
        verbose_name_plural = 'Autorizados'

    def __str__(self):
        text = '{} {}'.format(
            self.name,
            self.lastname,
        )
        return text

class Student_Withdraw_Authorized(BaseModel):

    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Alumno')
    withdraw_authorized = models.ForeignKey(Withdraw_Authorized, on_delete=models.CASCADE, verbose_name='Autorizado a retiro')
    RELATIONSHIP_CHOICES = [
        ('Hermano/a', 'Hermano/a'),
        ('Primo/a', 'Primo/a'),
        ('Tío/a', 'Tío/a'),
        ('Otro', 'Otro'),
    ]
    relationship = models.CharField(
        'Vínculo',
        max_length=15,
        choices = RELATIONSHIP_CHOICES,
        default='Hermano/a',
        )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['withdraw_authorized', 'student'], name='authorized_student_combination'
            )
        ]
        verbose_name = 'Autorizado_Alumno'
        verbose_name_plural = 'Autorizados_Alumnos'

    def __str__(self):
        text = '{} {} - {} {}'.format(
            self.withdraw_authorized.name,
            self.withdraw_authorized.lastname,
            self.student.first_name,
            self.student.first_lastname,
        )
        return text

class Payment(BaseModel):

    amount = models.IntegerField('Importe', blank=True, null=True)
    payment_date = models.DateField('Fecha de pago', auto_now=False, auto_now_add=False, blank=True, null=True)
    file = models.FileField('Comprobante', upload_to='documentos/alumnos/%Y', null=True)
    PAYMENT_CHOICES = [
        ('1', 'Cuota mensual'),
        ('2', 'Pago de matrícula'),
    ]
    payment_type = models.CharField(
        'Tipo de pago',
        max_length=1,
        choices = PAYMENT_CHOICES,
        default='1',
        )
    # BROTHERS_QTY_CHOICES = [
    #     ('1', '1'),
    #     ('2', '2'),
    #     ('3', '3'),
    #     ('4', '4'),
    #     ('5', '5'),
    # ]
    # brothers_qty = models.CharField(
    #     'Cantidad de hermanos',
    #     max_length=1,
    #     choices = BROTHERS_QTY_CHOICES,
    #     default='1',
    #     )
    # brothers_discount = models.IntegerField('Descuento por hermanos', blank=True, null=True)

    class Meta:
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'

    def __str__(self):
        text = '{} - {}'.format(
            self.id,
            self.payment_type,
        )
        return text

class Payment_Student (BaseModel):

    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Alumno')
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, verbose_name='Pago')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['payment', 'student'], name='payment_student_combination'
            )
        ]
        verbose_name = 'Pago_Alumno'
        verbose_name_plural = 'Pagos_Alumnos'

    def __str__(self):
        text = '{} {} - {} {}'.format(
            self.payment.id,
            self.payment.payment_type,
            self.student.first_name,
            self.student.first_lastname,
        )
        return text

class Student_Documents (BaseModel):

    student = models.ForeignKey('alumnos.Student', on_delete=models.CASCADE, verbose_name='Alumno')
    documents = models.ForeignKey('administracion.Documents', on_delete=models.CASCADE, verbose_name='Documentación')
    file = models.FileField('Documento', upload_to='documentos/alumnos/%Y')

    class Meta:
        verbose_name = 'Alumno_Documento'
        verbose_name_plural = 'Alumnos_Documentos'

    def __str__(self):
        text = '{} - {} - {} {}'.format(
            self.id,
            self.documents.document_type,
            self.student.first_name,
            self.student.first_lastname,
        )
        return text

