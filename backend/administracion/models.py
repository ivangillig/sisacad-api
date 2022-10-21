from django.db import models
from django.contrib.auth.models import User


class Rol(models.Model):
    
    id_rol = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    def __str__(self):
        texto = '{}'.format(
            self.nombre,
        )
        return texto

class Persona(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_rol = models.ForeignKey(Rol, on_delete=models.CASCADE, null=True)
    nombre1 = models.CharField(max_length=15)
    nombre2 = models.CharField(max_length=15, blank=True, null=True)
    apellido1 = models.CharField(max_length=15)
    apellido2 = models.CharField(max_length=15, blank=True, null=True)
    dni = models.CharField(max_length=13, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    lugar_nacimiento = models.CharField(max_length=15, blank=True, null=True)
    nacionalidad = models.CharField(max_length=15, blank=True, null=True)
    GENERO_OPCIONES = [
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
        ('Sin genero', 'Sin genero'),
    ]
    genero = models.CharField(
        max_length=20,
        choices = GENERO_OPCIONES,
        default='Masculino',
        blank=True, null=True
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
        blank=True, null=True
        )
    fecha_alta = models.DateField(blank=True, null=True)
    
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
        blank=True, null=True
        )
    email_institucional = models.EmailField(max_length=40, blank=True, null=True)
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
        blank=True, null=True,
        )


    def __str__(self):
        texto = '{}'.format(
            self.dni,
        )
        return texto

class Alumno(Persona):
    
    email_institucional = models.EmailField(max_length=40, blank=True, null=True)
    telefono_familiar = models.CharField(max_length=15, blank=True, null=True)
    tratamiento_medico = models.BooleanField(blank=True, null=True)
    medicamentos = models.TextField(max_length=200, blank=True, null=True)
    alergias = models.TextField(max_length=200, blank=True, null=True)
    observaciones = models.TextField(max_length=200, blank=True, null=True)
    cert_escolar_destino = models.CharField(max_length=30, blank=True, null=True)
    fecha_ingreso = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    fecha_baja = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    aut_paseos = models.BooleanField(blank=True, null=True)
    aut_medica = models.BooleanField(blank=True, null=True)
    aut_salida = models.BooleanField(blank=True, null=True)
    aut_publica = models.BooleanField(blank=True, null=True)

    def __str__(self):
        texto = '{} - {} {}'.format(
            self.user_id,
            self.apellido1,
            self.nombre1,
        )
        return texto

class Materia(models.Model):
    
    id_materia = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    fecha_alta = models.DateField(blank=True, null=True)
    fecha_baja = models.DateField(blank=True, null=True)

    def __str__(self):
        texto = '{} - {}'.format(
            self.id_materia,
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
        null=True,
        )

    def __str__(self):
        texto = '{}'.format(
            self.tipo_documentacion,
        )
        return texto

class Documentacion_Docente(models.Model):
    
    docente_id = models.ForeignKey(Docente, on_delete=models.CASCADE, null=True)
    documentacion_id = models.ForeignKey(Documentacion, on_delete=models.CASCADE, null=True)
    ruta_archivo = models.CharField(max_length=30, blank=True, null=True)
    fecha_ingreso = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)

    def __str__(self):
        texto = '{}'.format(
            self.documentacion_id,
        )
        return texto

class Tutor(models.Model):
    
    #id_tutor = models.ForeignKey(Usuario, on_delete=models.CASCADE, primary_key=True, unique=True) 
    TIPO_OPCIONES = [
        ('Madre', 'Madre'),
        ('Padre', 'Padre'),
        ('Tutor legal', 'Tutor legal'),
    ]
    estado = models.CharField(
        max_length=15,
        choices = TIPO_OPCIONES,
        default='Madre',
        null=True,
        )
    Profesion = models.CharField(max_length=15)
    domicilio_laboral = models.CharField(max_length=30)
    telefono_laboral = models.CharField(max_length=12)


    def __str__(self):
        texto = '{}'.format(
            self.dni,
        )
        return texto

class Division(models.Model):
    
    id_division = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=15, blank=True, null=True)
    STATUS_CHOICES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    ]
    estado = models.CharField(
        max_length=8,
        choices = STATUS_CHOICES,
        default='Activo',
        null=True,
        )

    def __str__(self):
        texto = '{} - {}'.format(
            self.id_division,
            self.nombre,
        )
        return texto

class Nivel(models.Model):
    
    id_nivel = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    STATUS_CHOICES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    ]
    estado = models.CharField(
        max_length=8,
        choices = STATUS_CHOICES,
        default='Activo',
        null=True,
        )

    def __str__(self):
        texto = '{} - {}'.format(
            self.id_nivel,
            self.nombre,
        )
        return texto

class Modalidad(models.Model):
    
    id_modalidad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    STATUS_CHOICES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    ]
    estado = models.CharField(
        max_length=8,
        choices = STATUS_CHOICES,
        default='Activo',
        null=True,
        )
    fecha_alta = models.DateField(blank=True, null=True)
    fecha_baja = models.DateField(blank=True, null=True)


    def __str__(self):
        texto = '{} - {}'.format(
            self.id_modalidad,
            self.nombre,
        )
        return texto

class Año(models.Model):
    id_año = models.AutoField(primary_key=True)
    id_nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE, null=True, blank=True)
    id_modalidad = models.ForeignKey(Modalidad, on_delete=models.CASCADE, null=True, blank=True)
    id_division = models.ForeignKey(Division, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=30, blank=True, null=True)
    STATUS_CHOICES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    ]
    estado = models.CharField(
        max_length=8,
        choices = STATUS_CHOICES,
        default='Activo',
        null=True,
        blank=True,
        )

    def __str__(self):
        texto = '{} {} {} - {}'.format(
            self.nombre,
            self.id_division.nombre,
            self.id_modalidad.nombre,
            self.id_nivel.nombre,
        )
        return texto

class Curso(models.Model):
    año = models.ForeignKey(Año, on_delete=models.CASCADE, null=True, blank=True)
    año_lectivo = models.IntegerField(blank=True, null=True)
    STATUS_CHOICES = [
        ('Mañana', 'Mañana'),
        ('Tarde', 'Tarde'),
        ('Noche', 'Noche'),
    ]
    turno = models.CharField(
        max_length=8,
        choices = STATUS_CHOICES,
        default='Mañana',
        null=True,
        blank=True,
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
            self.año.id_division.nombre,
            self.turno,
        )
        return texto

class CursoAlumnos(models.Model):
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True, blank=True)
    dni_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, null=True, blank=True)
    fecha_alta = models.DateField(blank=True, null=True)
    fecha_baja = models.DateField(blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['id_curso', 'dni_alumno'], name='curso_alumno_combinacion'
            )
        ]

    def __str__(self):
        texto = '{} {} {} - {} {}'.format(
            self.id_curso.año.nombre,
            self.id_curso.año.id_division.nombre,
            self.id_curso.año_lectivo,
            self.dni_alumno.apellido1,
            self.dni_alumno.nombre1,
        )
        return texto

class Post(models.Model):
    id_post = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=30)
    resumen = models.CharField(max_length=50)
    contenido = models.TextField(max_length=100)
    image = models.ImageField(upload_to ='uploads/')
    STATUS_CHOICES = [
        ('Publicado', 'Publicado'),
        ('Borrador', 'Borrador'),
    ]
    status = models.CharField(
        max_length=20,
        choices = STATUS_CHOICES,
        default='Borrador',
        )
    #id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True)
    #id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)

    def __str__(self):
        texto = '{}'.format(
            self.titulo,
        )
        return texto

class Comentario(models.Model):
    
    id_comentario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    comentario = models.TextField()
    email = models.EmailField(max_length=40)
    STATUS_CHOICES = [
        ('Publicado', 'Publicado'),
        ('Borrador', 'Borrador'),
    ]
    status = models.CharField(
        max_length=20,
        choices = STATUS_CHOICES,
        default='Borrador',
        )
    fecha_creado = models.DateField()
    id_post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)

    def __str__(self):
        texto = '{} {}'.format(
            self.nombre,
            self.email,
        )
        return texto