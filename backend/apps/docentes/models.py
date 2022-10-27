from django.db import models

from apps.users.models import Person
from apps.administracion.models import Documents

# Create your models here.
class Teacher(Person):
    
    cuil = models.CharField(max_length=15, blank=True, null=True)
    STATE_CHOICES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    ]
    state = models.CharField(
        'Estado',
        max_length=10,
        choices = STATE_CHOICES,
        default='Activo',
        )
    seniority_date = models.DateField('Fecha de antiguedad', blank=True, null=True)
    seniority_qty = models.IntegerField('Antiguedd reconocida', blank=True, null=True)
    STATISTICS_CHOICES = [
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
    statistics = models.CharField(
        'Estadística',
        max_length=50,
        choices = STATISTICS_CHOICES,
        default='En actividad',
        )

    class Meta:
        verbose_name = 'Docente'
        verbose_name_plural = 'Docentes'


    def __str__(self):
        text = '{}'.format(
            self.doc_number,
        )
        return text

class Teacher_Documents(models.Model):
    
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Docente')
    documents = models.ForeignKey(Documents, on_delete=models.CASCADE, verbose_name='Documentación')
    created_date = models.DateField('Fecha de ingreso', auto_now=False, auto_now_add=False, blank=True, null=True)

    class Meta:
        verbose_name = 'Docente_Documento'
        verbose_name_plural = 'Docentes_Documentos'

    def __str__(self):
        text = '{}'.format(
            self.id,
        )
        return text

