from django.db import models
from apps.base.models import BaseModel

#aux
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _

####################################
############# MATERIAS #############
####################################

class Subject(BaseModel):

    name = models.CharField('Nombre de materia', max_length=30, unique=True)

    class Meta:
        verbose_name = 'Materia'
        verbose_name_plural = 'Materias'

    def __str__(self):
        text= '{} - {}'.format(
            self.id,
            self.name,
        )
        return text

class Documents(BaseModel):
    
    document_type = models.CharField('Tipo de documento', max_length=30, unique=True)
    #role = models.ForeignKey("User.role", verbose_name=_("Usuarios"), on_delete=models.CASCADE, null=True)
    
    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'

    def __str__(self):
        text = '{}'.format(
            self.document_type,
        )
        return text


####################################
#### ATRIBUTOS DEL AÑO LECTIVO #####
####################################

class Division(BaseModel):
    
    name = models.CharField('Nombre', max_length=15, unique=True)

    class Meta:
        verbose_name = 'División'
        verbose_name_plural = 'Divisiones'

    def __str__(self):
        text = '{}'.format(
            self.name,
        )
        return text

class Level(BaseModel): 
    
    #docente = models.ForeignKey(Docente, related_name='docente', on_delete=models.CASCADE, null=True)
    name = models.CharField('Nombre', max_length=30, unique=True)

    class Meta:
        verbose_name = 'Nivel'
        verbose_name_plural = 'Niveles'

    def __str__(self):
        text = '{}'.format(
            self.name,
        )
        return text

class Speciality(BaseModel):
    
    name = models.CharField('Nombre', max_length=40, unique=True)
    shortName = models.CharField('Nombre_corto', max_length=12, blank=True, null=True)

    class Meta:
        verbose_name = 'Modalidad'
        verbose_name_plural = 'Modalidades'


    def __str__(self):
        text = '{}'.format(
            self.name,
        )
        return text

class Grade(BaseModel):
    
    level = models.ForeignKey(Level, on_delete=models.CASCADE, verbose_name='Nivel')
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, verbose_name='Modalidad', blank=True, null=True)
    division = models.ForeignKey(Division, on_delete=models.CASCADE, verbose_name='División', blank=True, null=True)
    name = models.CharField('Nombre', max_length=30)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'division'], name='name_division_combination'
            )
        ]
        verbose_name = 'Año'
        verbose_name_plural = 'Años'

    def __str__(self):
        text = '{} {} - {}'.format(
        self.name,
        self.level.name,
        self.division.name
        )
        return text


import datetime
def current_year():
        return datetime.date.today().year

def max_value_current_year(value):
        return MaxValueValidator(current_year())(value)  


####################################
####### CURSO Y ESTUDIANTES ########
####################################

class Course(BaseModel):
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
        text = '{} {} - Ciclo {}'.format(
            self.grade.name,
            self.grade.division.name,
            self.academic_year,
        )
        return text

class Course_Student(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Curso')
    student = models.ForeignKey('alumnos.Student', on_delete=models.CASCADE, verbose_name='Alumno')
    add_date = models.DateField('Fecha de ingreso')
    leaving_date = models.DateField('Fecha de salida', blank=True, null=True)
    LEAVING_MOTIVE_CHOICES = [
        ('Finalización de año', 'Finalización de año'),
        ('Pase', 'Pase'),
        ('Fallecimiento', 'Fallecimiento'),
    ]
    leaving_motive = models.CharField(
        'Motivo de baja',
        max_length=30,
        choices = LEAVING_MOTIVE_CHOICES,
        null=True,
        blank=True,
        #default='Finalización de año',
        )

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

####################################
### CARGOS DOCENTES / CATEGORIAS ###
####################################

class Category (BaseModel):
    
    category_id = models.IntegerField('Código de categoría', primary_key=True)
    name = models.CharField('Nombre', max_length=50, unique=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        text = '{} - {}'.format(
            self.category_id,
            self.name,
        )
        return text

class Position (BaseModel):
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoría')
    place_number1 = models.IntegerField('Nro de plaza 1', blank=True, null=True)
    place_number2 = models.IntegerField('Nro de plaza 2', blank=True, null=True)
    hours_qty = models.IntegerField('Cantidad de horas', blank=True, null=True)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        text = 'Nro Pza: {} - {} {}'.format(
            self.place_number1,
            self.category.category_id,
            self.category.name
        )
        return text


class Position_Teacher(BaseModel):
    
    teacher = models.ForeignKey('docentes.Teacher', on_delete=models.CASCADE, verbose_name='Docente', null=True)
    position = models.ForeignKey('administracion.Position', on_delete=models.CASCADE, verbose_name='Cargo')
    POSITION_TYPE_CHOICES = [
        ('Titular', 'Titular'),
        ('Suplente', 'Suplente'),
    ]
    position_type = models.CharField(
        'Tipo de cargo',
        max_length=8,
        choices = POSITION_TYPE_CHOICES,
        default='Vacante',
        )
    condition = models.CharField('Situación', max_length=15, blank=True, null=True)
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
########## INFO BANCARIA ###########
####################################

class Bank(BaseModel):
    
    bank_name = models.CharField('Nombre de banco', max_length=40, unique=True)

    class Meta:
        verbose_name = 'Banco'
        verbose_name_plural = 'Bancos'

    def __str__(self):
        text = '{} - {}'.format(
            self.id,
            self.bank_name,
        )
        return text


###################################

class Course_Subject(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Curso')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='Materia')
    position_teacher = models.ForeignKey(Position_Teacher, on_delete=models.CASCADE, verbose_name='Cargo_Docente')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['course', 'subject'], name='course_subject_combination'
            )
        ]
        verbose_name = 'Curso_Materia'
        verbose_name_plural = 'Cursos_Materias'

    def __str__(self):
        text = '{} {} {} - {} - {} {}'.format(
            self.course.grade.name,
            self.course.grade.division.name,
            self.course.academic_year,
            self.subject.name,
            self.position_teacher.teacher.first_name,
            self.position_teacher.teacher.first_lastname,
        )
        return text