from django.db import models
#from alumnos.models import Alumno
from django.conf import settings

#aux
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _


class Rol(models.Model):
    
    nombre = models.CharField(max_length=30)

    def __str__(self):
        texto = '{}'.format(
            self.nombre,
        )
        return texto

class Persona(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    nombre1 = models.CharField(max_length=15)
    nombre2 = models.CharField(max_length=15, blank=True, null=True)
    apellido1 = models.CharField(max_length=15)
    apellido2 = models.CharField(max_length=15, blank=True, null=True)
    dni = models.CharField(max_length=13)
    email_personal = models.EmailField(max_length=40, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    lugar_nacimiento = models.CharField(max_length=15, blank=True, null=True)
    nacionalidad = models.CharField(max_length=15, blank=True, null=True)
    GENERO_OPCIONES = [
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
        ('Sin genero', 'Sin genero'),
        ('Sin especificar', 'Sin especificar'),
    ]
    genero = models.CharField(
        max_length=20,
        choices = GENERO_OPCIONES,
        default='Sin especificar',
        )
    direccion = models.CharField(max_length=15, blank=True, null=True)
    barrio = models.CharField(max_length=15, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    OPCIONES_CIVIL = [
        ('Soltero', 'Soltero'),
        ('Casado', 'Casado'),
        ('Divorciado', 'Divorciado'),
        ('Viudo/a', 'Viudo/a'),
        ('No aplica', 'No aplica'),
    ]
    estado_civil = models.CharField(
        max_length=20,
        choices = OPCIONES_CIVIL,
        default='No aplica',
        )
    fecha_alta = models.DateField()
    
    def __str__(self):
        texto = '{} {}'.format(
            self.nombre1,
            self.apellido1,
        )
        return texto

class Docente(Persona):
    
    cuil = models.CharField(max_length=15, blank=True, null=True)
    ESTADO_OPCIONES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    ]
    estado = models.CharField(
        max_length=10,
        choices = ESTADO_OPCIONES,
        default='Activo',
        )
    fecha_antiguedad = models.DateField(blank=True, null=True)
    antiguedad_reconocida = models.IntegerField(blank=True, null=True)
    ESTADISTICA_OPCIONES = [
        ('En actividad', 'En actividad'),
        ('Tareas pasivas', 'Tareas pasivas'),
        ('Docentes afectados al JIF pero de otra POF', 'Docentes afectados al JIF pero de otra POF'),
        ('Docentes del JIF afectados a otro establecimiento', 'Docentes del JIF afectados a otro establecimiento'),
        ('Sin subvención', 'Sin subvención'),
        ('Baja', 'Baja'),
        ('Fuera de actividad', 'InaFuera de actividadctivo'),
        ('A.T. / Integrador', 'A.T. / Integrador'),
        ('Par pedagógico / Dep. de dirección privada', 'Par pedagógico / Dep. de dirección privada'),
    ]
    estadistica = models.CharField(
        max_length=50,
        choices = ESTADISTICA_OPCIONES,
        default='En actividad',
        )


    def __str__(self):
        texto = '{}'.format(
            self.dni,
        )
        return texto



class Materia(models.Model):

    nombre = models.CharField(max_length=30, unique=True)
    fecha_alta = models.DateField()
    fecha_baja = models.DateField(blank=True, null=True)

    def __str__(self):
        texto = '{} - {}'.format(
            self.id,
            self.nombre,
        )
        return texto

class Documentacion(models.Model):
    
    TIPO_OPCIONES = [
        ('DNI', 'DNI'),
        ('Certificado', 'Certificado'),
        ('Constancia 1', 'Constancia 1'),
        ('Constancia 2', 'Constancia 2'),
    ]
    tipo_documentacion = models.CharField(
        max_length=15,
        choices = TIPO_OPCIONES,
        default='DNI',
        )

    def __str__(self):
        texto = '{}'.format(
            self.tipo_documentacion,
        )
        return texto

class Documentacion_Docente(models.Model):
    
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    documentacion = models.ForeignKey(Documentacion, on_delete=models.CASCADE)
    fecha_ingreso = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)

    def __str__(self):
        texto = '{}'.format(
            self.id,
        )
        return texto



    def __str__(self):
        texto = '{} {}'.format(
            self.nombre1,
            self.apellido1,
        )
        return texto



class Division(models.Model):
    
    nombre = models.CharField(max_length=15, unique=True)
    STATUS_CHOICES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
        ('N/A', 'N/A'),
    ]
    estado = models.CharField(
        max_length=8,
        choices = STATUS_CHOICES,
        default='N/A',
        )
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        texto = '{} - {}'.format(
            self.id,
            self.nombre,
        )
        return texto

class Nivel(models.Model):
    
    #docente = models.ForeignKey(Docente, related_name='docente', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=30, unique=True)
    STATUS_CHOICES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    ]
    estado = models.CharField(
        max_length=8,
        choices = STATUS_CHOICES,
        default='Activo',
        )
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        texto = '{} - {}'.format(
            self.id,
            self.nombre,
        )
        return texto

class Modalidad(models.Model):
    
    nombre = models.CharField(max_length=30, unique=True)
    STATUS_CHOICES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
        ('N/A', 'N/A'),
    ]
    estado = models.CharField(
        max_length=8,
        choices = STATUS_CHOICES,
        default='N/A',
        null=True,
        )
    fecha_alta = models.DateField(blank=True, null=True)
    fecha_baja = models.DateField(blank=True, null=True)


    def __str__(self):
        texto = '{} - {}'.format(
            self.id,
            self.nombre,
        )
        return texto

class Año(models.Model):
    
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)
    modalidad = models.ForeignKey(Modalidad, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30, unique=True)
    STATUS_CHOICES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    ]
    estado = models.CharField(
        max_length=8,
        choices = STATUS_CHOICES,
        default='Activo',
        )

    def __str__(self):
        texto = '{} {} {} - {}'.format(
            self.nombre,
            self.division.nombre,
            self.modalidad.nombre,
            self.nivel.nombre,
        )
        return texto

import datetime
def current_year():
        return datetime.date.today().year

def max_value_current_year(value):
        return MaxValueValidator(current_year())(value)  



class Curso(models.Model):
    año = models.ForeignKey(Año, on_delete=models.CASCADE)

    #año_lectivo = models.IntegerField()

    año_lectivo = models.IntegerField(validators=[MinValueValidator(1984), max_value_current_year])

    STATUS_CHOICES = [
        ('Mañana', 'Mañana'),
        ('Tarde', 'Tarde'),
        ('Noche', 'Noche'),
        ('Sin definir', 'Sin definir'),
    ]
    turno = models.CharField(
        max_length=11,
        choices = STATUS_CHOICES,
        default='Sin definir',
        )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['año', 'año_lectivo'], name='id_curso_combinacion'
            )
        ]

    def __str__(self):
        texto = '{} {} - Turno {}'.format(
            self.año.nombre,
            self.año.division.nombre,
            self.turno,
        )
        return texto

class Curso_Alumno(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    alumno = models.ForeignKey('alumnos.Alumno', on_delete=models.CASCADE)
    fecha_alta = models.DateField(blank=True, null=True)
    fecha_baja = models.DateField(blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['curso', 'alumno'], name='curso_alumno_combinacion'
            )
        ]

    def __str__(self):
        texto = '{} {} {} - {} {}'.format(
            self.curso.año.nombre,
            self.curso.año.id_division.nombre,
            self.curso.año_lectivo,
            self.alumno.apellido1,
            self.alumno.nombre1,
        )
        return texto
