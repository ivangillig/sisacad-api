#from pyexpat import model

from django.db import models
from apps.users.models import Person
from apps.base.models import BaseModel

from simple_history.models import HistoricalRecords

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

####################################
###### LICENCIAS Y PERMISOS ########
####################################

class License(models.Model):
    
    license_type = models.CharField('Tipo de licencia', max_length=30, unique=True, null=True)
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

class Permission_Request(models.Model):
    
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Docente')
    motive = models.CharField('Motivo del permiso', max_length=100)
    request_date = models.DateField('Fecha de solicitud', auto_now_add=True)
    permission_date = models.DateField('Fecha de salida', auto_now=False, auto_now_add=False, blank=True, null=True)
    permission_checkin = models.TimeField('Hora de salida', auto_now=False, auto_now_add=False, blank=True, null=True)
    permission_checkout = models.TimeField('Hora de entrada', auto_now=False, auto_now_add=False, blank=True, null=True)
    STATUS_CHOICES = [
        ('1', 'Pendiente de autorización'),
        ('2', 'Aprobado'),
        ('3', 'Rechazado'),
    ]
    status = models.CharField(
        'Estado',
        max_length=2,
        choices = STATUS_CHOICES,
        default='1',
        )
    rejected_motive = models.CharField('Motivo de rechazo', max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Solicitud_Permiso'
        verbose_name_plural = 'Solicitudes_Permisos'

    def __str__(self):
        text = '{} - {} - {} {}'.format(
            self.id,
            self.request_date,
            self.teacher.first_name,
            self.teacher.first_lastname,
        )
        return text

####################################
#### DATOS BANCARIOS Y RECIBOS #####
####################################

class Salary_Receipt(models.Model):
    
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Docente')
    receipt_file = models.FileField('Documentos/Certificados', upload_to='documentos/recibos', null=True, blank=True)
    created_date = models.DateField('Fecha de registro', auto_now=False, auto_now_add=False, blank=True, null=True)
    MONTH_CHOICES = [
        ('1', 'Enero'),
        ('2', 'Febrero'),
        ('3', 'Marzo'),
        ('4', 'Abril'),
        ('5', 'Mayo'),
        ('6', 'Junio'),
        ('7', 'Julio'),
        ('8', 'Agosto'),
        ('9', 'Septiembre'),
        ('10', 'Octubre'),
        ('11', 'Noviembre'),
        ('12', 'Diciembre'),
    ]
    receipt_month = models.CharField(
        'Mes de recibo',
        max_length=2,
        choices = MONTH_CHOICES,
        default='1',
        )

    class Meta:
        verbose_name = 'Recibo de haber'
        verbose_name_plural = 'Recibos de haberes'

    def __str__(self):
        text = '{} - {} {} - {} {}'.format(
            self.id,
            self.teacher.first_name,
            self.teacher.first_lastname,
            self.created_date,
            self.receipt_month,
        )
        return text

class Bank_Account (models.Model):
    
    cbu = models.CharField('CBU', max_length=22, unique=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Docente')
    bank = models.ForeignKey('administracion.Bank', on_delete=models.CASCADE, verbose_name='Banco')
    account_number = models.CharField('Nro de cuenta', max_length=22, null=True, blank=True)
    created_date = models.DateField('Fecha de alta', auto_now=False, auto_now_add=False, blank=True, null=True)
    state = models.BooleanField('Vigente', max_length=1, default=True)

    class Meta:
        verbose_name = 'Cuenta_Banco'
        verbose_name_plural = 'Cuentas_Bancos'

    def __str__(self):
        text = '{} {} - {} - {}'.format(
            self.teacher.first_name,
            self.teacher.first_lastname,
            self.bank.bank_name,
            self.cbu,
        )
        return text

####################################
############# TITULOS  #############
####################################

class Degree(models.Model):
    
    degree_name = models.CharField('Título', max_length=40, unique=True)
    created_date = models.DateField('Fecha de ingreso', auto_now_add=True)

    class Meta:
        verbose_name = 'Título'
        verbose_name_plural = 'Títulos'

    def __str__(self):
        text = '{} - {}'.format(
            self.id,
            self.degree_name,
        )
        return text

class Teacher_Degree(models.Model):
    
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Docente')
    degree = models.ForeignKey('docentes.Degree', on_delete=models.CASCADE, verbose_name='Título')
    file = models.FileField('Foto/Escaneo de Título', upload_to='documentos/titulos', null=True, blank=True)
    graduated_date = models.DateField('Fecha de graduación', auto_now=False, auto_now_add=False, blank=True, null=True)
    institution = models.CharField('Otorgado por', max_length=30, blank=True, null=True)
    created_date = models.DateField('Fecha de registro', auto_now_add=True)

    class Meta:
        verbose_name = 'Docente_Titulo'
        verbose_name_plural = 'Docentes_Titulos'

    def __str__(self):
        text = '{} - {} {}'.format(
            self.id,
            self.teacher.first_name,
            self.teacher.first_lastname,
        )
        return text


####################################
########## Disponibilidad ##########
####################################

class Disponibility (BaseModel):
    
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='Docente')
    DAY_CHOICES = [
        ('1', 'Lunes'),
        ('2', 'Martes'),
        ('3', 'Miercoles'),
        ('4', 'Jueves'),
        ('5', 'Viernes'),
    ]
    week_day = models.CharField(
        'Día de la semana',
        max_length=1,
        choices = DAY_CHOICES,
        default='1',
        )
    init_time = models.TimeField('Hora inicio', auto_now=False, auto_now_add=False, blank=True, null=True)
    end_time = models.TimeField('Hora fin', auto_now=False, auto_now_add=False, blank=True, null=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Disponibilidad horaria'
        verbose_name_plural = 'Disponibilidad horaria'

    def __str__(self):
        text = '{} - {} {}'.format(
            self.id,
            self.teacher.first_name,
            self.teacher.first_lastname,
        )
        return text