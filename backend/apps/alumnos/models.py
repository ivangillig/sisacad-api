from django.db import models
from django.conf import settings
from apps.administracion.models import Person

# Create your models here.
class Student(Person):
    
    family_phone = models.CharField('Teléfono familiar', max_length=15, blank=True, null=True)
    medical_treatment = models.BooleanField('Tratamiento médico', blank=True, null=True)
    medications = models.TextField('Medicamentos', max_length=200, blank=True, null=True)
    allergies = models.TextField('Alergias', max_length=200, blank=True, null=True)
    observations = models.TextField('Observaciones', max_length=200, blank=True, null=True)
    school_cert_destinty = models.CharField('Destino de certificado escolar', max_length=30, blank=True, null=True)
    admission_date = models.DateField('Fecha de ingreso', auto_now=False, auto_now_add=False, blank=True, null=True)
    leaving_date = models.DateField('Fecha de baja', auto_now=False, auto_now_add=False, blank=True, null=True)
    trips_auth = models.BooleanField('Autorización de paseos', default=False)
    medical_auth = models.BooleanField('Autorización médica', default=False)
    leave_auth = models.BooleanField('Autorización de salida', default=False)
    public_auth = models.BooleanField('Autorización para publicar', default=False)

    def __str__(self):
        text = '{} - {} {}'.format(
            self.user_id,
            self.first_lastname,
            self.firstname,
        )
        return text

class Tutor(Person):

    profession = models.CharField('Profesión', max_length=15, blank=True, null=True)
    job_address = models.CharField('Domicilio laboral', max_length=30, blank=True, null=True)
    job_phone = models.CharField('Teléfono laboral', max_length=12, blank=True, null=True)

    def __str__(self):
        text = '{} {}'.format(
            self.first_name,
            self.first_lastname,
        )
        return text

class Student_Tutor(models.Model):

    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Alumno')

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

    def __str__(self):
        text = '{}'.format(
            self.relationship,
        )
        return text

