from pyexpat import model
from django.db import models

from apps.users.models import Person

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
        text = '{} - {} {}'.format(
            self.doc_number,
            self.first_name,
            self.first_lastname
        )
        return text

class Teacher_Documents(models.Model):
    
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Docente')
    documents = models.ForeignKey('administracion.Documents', on_delete=models.CASCADE, verbose_name='Documentación')
    file = models.FileField('Documento', upload_to='documentos/alumnos/%Y', null=True)
    created_date = models.DateField('Fecha de ingreso', auto_now=False, auto_now_add=False, blank=True, null=True)

    class Meta:
        verbose_name = 'Docente_Documento'
        verbose_name_plural = 'Docentes_Documentos'

    def __str__(self):
        text = '{} - {} - {} {}'.format(
            self.id,
            self.documents.document_type,
            self.student.first_name,
            self.student.first_lastname,
        )
        return text

class Position_Teacher(models.Model):
    
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Docente')
    position = models.ForeignKey('administracion.Position', on_delete=models.CASCADE, verbose_name='Cargo')
    POSITION_TYPE_CHOICES = [
        ('Titular', 'Titular'),
        ('Suplente', 'Suplente'),
    ]
    position_type = models.CharField(
        'Tipo de cargo',
        max_length=8,
        choices = POSITION_TYPE_CHOICES,
        default='Titular',
        )
    condition = models.CharField('Situación', max_length=15, blank=True, null=True)
    created_date = models.DateField('Fecha de alta', auto_now=False, auto_now_add=False, blank=True, null=True)
    deleted_date = models.DateField('Fecha de baja', auto_now=False, auto_now_add=False, blank=True, null=True)
    delete_motive = models.CharField('Motivo de baja', max_length=150, blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['position', 'position_type'], name='position_type_combination'
            )
        ]
        verbose_name = 'Cargo_Docente'
        verbose_name_plural = 'Cargos_Docentes'

    def __str__(self):
        text = '{} - {} {} - {}'.format(
            self.position.place_number1,
            self.teacher.first_name,
            self.teacher.first_lastname,
            self.position_type
        )
        return text

################################

class License(models.Model):
    
    license_type = models.CharField('Tipo de licencia', max_length=30, blank=True, null=True, unique=True)
    created_date = models.DateField('Fecha de ingreso', auto_now=False, auto_now_add=False, blank=True, null=True)

    class Meta:
        verbose_name = 'Licencia'
        verbose_name_plural = 'Licencias'

    def __str__(self):
        text = '{} - {}'.format(
            self.id,
            self.license_type,
        )
        return text

class Teacher_License(models.Model):
    
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Docente')
    license = models.ForeignKey('docentes.License', on_delete=models.CASCADE, verbose_name='Licencia')
    file = models.FileField('Documentos/Certificados', upload_to='documentos/licencias', null=True, blank=True)
    created_date = models.DateField('Fecha de registro', auto_now=False, auto_now_add=False, blank=True, null=True)
    is_paid = models.BooleanField('Con goce de sueldo', max_length=150, default=False)
    license_from = models.DateField('Licencia desde', auto_now=False, auto_now_add=False, blank=True, null=True)
    license_to = models.DateField('Licencia hasta', auto_now=False, auto_now_add=False, blank=True, null=True)

    class Meta:
        verbose_name = 'Docente_Licencia'
        verbose_name_plural = 'Docentes_Licencias'

    def __str__(self):
        text = '{} - {} - {} {}'.format(
            self.id,
            self.license.license_type,
            self.teacher.first_name,
            self.teacher.first_lastname,
        )
        return text