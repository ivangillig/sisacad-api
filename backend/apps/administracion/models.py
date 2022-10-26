from django.db import models
from django.conf import settings

#aux
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _


class Role(models.Model):
    
    name = models.CharField('Nombre', max_length=30)

    def __str__(self):
        texto = '{}'.format(
            self.name,
        )
        return texto

class Person(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, verbose_name='Rol')
    first_name = models.CharField('Primer nombre', max_length=15)
    middle_name = models.CharField('Segundo nombre', max_length=15, blank=True, null=True)
    first_lastname = models.CharField('Primer apellido', max_length=15)
    second_lastname = models.CharField('Segundo apellido', max_length=15, blank=True, null=True)
    doc_number = models.CharField('DNI', max_length=13)
    personal_email = models.EmailField('Email personal', max_length=40, blank=True, null=True)
    birthday = models.DateField('Fecha de nacimiento', blank=True, null=True)
    birth_place = models.CharField('Lugar de nacimiento', max_length=15, blank=True, null=True)
    nationality = models.CharField('Nacionalidad', max_length=15, blank=True, null=True)
    CHOICES_GENDER = [
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
        ('Sin genero', 'Sin genero'),
        ('Sin especificar', 'Sin especificar'),
    ]
    gender = models.CharField(
        'Género',
        max_length=20,
        choices = CHOICES_GENDER,
        default='Sin especificar',
        )
    address = models.CharField('Dirección', max_length=15, blank=True, null=True)
    neighborhood = models.CharField('Barrio', max_length=15, blank=True, null=True)
    phone = models.CharField('Nro de teléfono', max_length=15, blank=True, null=True)
    STATE_CHOICES = [
        ('Soltero', 'Soltero'),
        ('Casado', 'Casado'),
        ('Divorciado', 'Divorciado'),
        ('Viudo/a', 'Viudo/a'),
        ('No aplica', 'No aplica'),
    ]
    marital_status = models.CharField(
        'Estado civil',
        max_length=20,
        choices = STATE_CHOICES,
        default='No aplica',
        )
    created_date = models.DateField('Fecha de alta')

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        ordering = ['first_name']
    
    def __str__(self):
        texto = '{} {}'.format(
            self.first_name,
            self.first_lastname,
        )
        return texto

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


class Subject(models.Model):

    name = models.CharField('Nombre de materia', max_length=30, unique=True)
    created_date = models.DateField('Fecha de creación')
    deleted_date = models.DateField('Fecha de eliminación', blank=True, null=True)

    class Meta:
        verbose_name = 'Materia'
        verbose_name_plural = 'Materias'

    def __str__(self):
        text= '{} - {}'.format(
            self.id,
            self.name,
        )
        return text
class Documents(models.Model):
    
    TYPE_CHOICES = [
        ('DNI', 'DNI'),
        ('Certificado', 'Certificado'),
        ('Constancia 1', 'Constancia 1'),
        ('Constancia 2', 'Constancia 2'),
    ]
    document_type = models.CharField(
        'Tipo de documentación',
        max_length=15,
        choices = TYPE_CHOICES,
        default='DNI',
        )
    
    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'

    def __str__(self):
        text = '{}'.format(
            self.document_type,
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

class Division(models.Model):
    
    name = models.CharField('Nombre', max_length=15, unique=True)
    STATE_CHOICES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    ]
    state = models.CharField(
        'Estado', 
        max_length=8,
        choices = STATE_CHOICES,
        default='Activo',
        )
    created_date = models.DateField('Fecha de creación', auto_now_add=True)

    class Meta:
        verbose_name = 'División'
        verbose_name_plural = 'Divisiones'

    def __str__(self):
        text = '{} - {}'.format(
            self.id,
            self.name,
        )
        return text

class Level(models.Model): ## Level o Grade ???
    
    #docente = models.ForeignKey(Docente, related_name='docente', on_delete=models.CASCADE, null=True)
    name = models.CharField('Nombre', max_length=30, unique=True)
    STATE_CHOICES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    ]
    state = models.CharField(
        'Estado',
        max_length=8,
        choices = STATE_CHOICES,
        default='Activo',
        )
    created_date = models.DateField('Fecha de creación', auto_now_add=True)

    class Meta:
        verbose_name = 'Nivel'
        verbose_name_plural = 'Niveles'

    def __str__(self):
        text = '{} - {}'.format(
            self.id,
            self.name,
        )
        return text

class Speciality(models.Model):
    
    name = models.CharField('Nombre', max_length=30, unique=True)
    STATE_CHOICES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
        ('N/A', 'N/A'),
    ]
    state = models.CharField(
        'Estado',
        max_length=8,
        choices = STATE_CHOICES,
        default='N/A',
        )
    created_date = models.DateField('Fecha de alta', blank=True, null=True)
    leaving_date = models.DateField('Fecha de baja', blank=True, null=True)

    class Meta:
        verbose_name = 'Modalidad'
        verbose_name_plural = 'Modalidades'


    def __str__(self):
        text = '{} - {}'.format(
            self.id,
            self.name,
        )
        return text

class Grade(models.Model):
    
    level = models.ForeignKey(Level, on_delete=models.CASCADE, verbose_name='Nivel')
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, verbose_name='Modalidad', blank=True, null=True)
    division = models.ForeignKey(Division, on_delete=models.CASCADE, verbose_name='División', blank=True, null=True)
    name = models.CharField('Nombre', max_length=30, unique=True)
    STATE_CHOICES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    ]
    state = models.CharField(
        'Estado',
        max_length=8,
        choices = STATE_CHOICES,
        default='Activo',
        )

    class Meta:
        verbose_name = 'Año'
        verbose_name_plural = 'Años'

    def __str__(self):
        # if self.division.name is not None or self.speciality.name is not None:
        #     text = '{} {} {} - {}'.format(
        #     self.name,
        #     self.division.name,
        #     self.speciality.name,
        #     self.level.name,
        #     )
        # else:
        text = '{} - {}'.format(
        self.name,
        self.level.name
        )
        return text


import datetime
def current_year():
        return datetime.date.today().year

def max_value_current_year(value):
        return MaxValueValidator(current_year())(value)  

class Course(models.Model):
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, verbose_name='Año')
    academic_year = models.IntegerField('Año lectivo', validators=[MinValueValidator(1984), max_value_current_year])

    SHIFT_CHOICES = [
        ('Mañana', 'Mañana'),
        ('Tarde', 'Tarde'),
        ('Noche', 'Noche'),
        ('Sin definir', 'Sin definir'),
    ]
    shift = models.CharField(
        'Turno',
        max_length=11,
        choices = SHIFT_CHOICES,
        default='Sin definir',
        )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['grade', 'academic_year'], name='id_course_combination'
            )
        ]
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        text = '{} {} - Turno {}'.format(
            self.grade.name,
            self.grade.division.name,
            self.shift,
        )
        return text

class Course_Student(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Curso')
    student = models.ForeignKey('alumnos.Student', on_delete=models.CASCADE, verbose_name='Alumno')
    created_date = models.DateField('Fecha de alta', blank=True, null=True)
    leaving_date = models.DateField('Fecha de baja', blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['course', 'student'], name='course_student_combination'
            )
        ]
        verbose_name = 'Curso_Alumno'
        verbose_name_plural = 'Cursos_Alumnos'

    def __str__(self):
        text = '{} {} {} - {} {}'.format(
            self.course.grade.name,
            self.course.grade.division.name,
            self.course.academic_year,
            self.student.first_lastname,
            self.student.first_name,
        )
        return text
