from django.db import models
from django.conf import settings
from administracion.models import Persona

# Create your models here.
class Alumno(Persona):
    
    telefono_familiar = models.CharField(max_length=15, blank=True, null=True)
    tratamiento_medico = models.BooleanField(blank=True, null=True)
    medicamentos = models.TextField(max_length=200, blank=True, null=True)
    alergias = models.TextField(max_length=200, blank=True, null=True)
    observaciones = models.TextField(max_length=200, blank=True, null=True)
    cert_escolar_destino = models.CharField(max_length=30, blank=True, null=True)
    fecha_ingreso = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    fecha_baja = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    aut_paseos = models.BooleanField(default=False)
    aut_medica = models.BooleanField(default=False)
    aut_salida = models.BooleanField(default=False)
    aut_publica = models.BooleanField(default=False)

    def __str__(self):
        texto = '{} - {} {}'.format(
            self.user_id,
            self.apellido1,
            self.nombre1,
        )
        return texto

class Tutor(Persona):

    Profesion = models.CharField(max_length=15, blank=True, null=True)
    domicilio_laboral = models.CharField(max_length=30, blank=True, null=True)
    telefono_laboral = models.CharField(max_length=12, blank=True, null=True)

class Tutor_Alumno(models.Model):

    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)

    TIPO_OPCIONES = [
        ('Madre', 'Madre'),
        ('Padre', 'Padre'),
        ('Tutor legal', 'Tutor legal'),
    ]
    vinculo = models.CharField(
        max_length=15,
        choices = TIPO_OPCIONES,
        default='Tutor legal',
        )
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['tutor', 'alumno'], name='tutor_alumno_combinacion'
            )
        ]

    def __str__(self):
        texto = '{}'.format(
            self.vinculo,
        )
        return texto

