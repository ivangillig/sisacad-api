# Generated by Django 4.1.2 on 2022-10-23 20:08

import administracion.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Año',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, unique=True)),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('año_lectivo', models.IntegerField(validators=[django.core.validators.MinValueValidator(1984), administracion.models.max_value_current_year])),
                ('turno', models.CharField(choices=[('Mañana', 'Mañana'), ('Tarde', 'Tarde'), ('Noche', 'Noche'), ('Sin definir', 'Sin definir')], default='Sin definir', max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Curso_Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_alta', models.DateField(blank=True, null=True)),
                ('fecha_baja', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15, unique=True)),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo'), ('N/A', 'N/A')], default='N/A', max_length=8)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Documentacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_documentacion', models.CharField(choices=[('DNI', 'DNI'), ('Certificado', 'Certificado'), ('Constancia 1', 'Constancia 1'), ('Constancia 2', 'Constancia 2')], default='DNI', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Documentacion_Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_ingreso', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, unique=True)),
                ('fecha_alta', models.DateField()),
                ('fecha_baja', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Modalidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, unique=True)),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo'), ('N/A', 'N/A')], default='N/A', max_length=8, null=True)),
                ('fecha_alta', models.DateField(blank=True, null=True)),
                ('fecha_baja', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, unique=True)),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=8)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre1', models.CharField(max_length=15)),
                ('nombre2', models.CharField(blank=True, max_length=15, null=True)),
                ('apellido1', models.CharField(max_length=15)),
                ('apellido2', models.CharField(blank=True, max_length=15, null=True)),
                ('dni', models.CharField(max_length=13)),
                ('email_personal', models.EmailField(blank=True, max_length=40, null=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('lugar_nacimiento', models.CharField(blank=True, max_length=15, null=True)),
                ('nacionalidad', models.CharField(blank=True, max_length=15, null=True)),
                ('genero', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Sin genero', 'Sin genero'), ('Sin especificar', 'Sin especificar')], default='Sin especificar', max_length=20)),
                ('direccion', models.CharField(blank=True, max_length=15, null=True)),
                ('barrio', models.CharField(blank=True, max_length=15, null=True)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('estado_civil', models.CharField(choices=[('Soltero', 'Soltero'), ('Casado', 'Casado'), ('Divorciado', 'Divorciado'), ('Viudo/a', 'Viudo/a'), ('No aplica', 'No aplica')], default='No aplica', max_length=20)),
                ('fecha_alta', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tutor_Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vinculo', models.CharField(choices=[('Madre', 'Madre'), ('Padre', 'Padre'), ('Tutor legal', 'Tutor legal')], default='Tutor legal', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='administracion.persona')),
                ('telefono_familiar', models.CharField(blank=True, max_length=15, null=True)),
                ('tratamiento_medico', models.BooleanField(blank=True, null=True)),
                ('medicamentos', models.TextField(blank=True, max_length=200, null=True)),
                ('alergias', models.TextField(blank=True, max_length=200, null=True)),
                ('observaciones', models.TextField(blank=True, max_length=200, null=True)),
                ('cert_escolar_destino', models.CharField(blank=True, max_length=30, null=True)),
                ('fecha_ingreso', models.DateField(blank=True, null=True)),
                ('fecha_baja', models.DateField(blank=True, null=True)),
                ('aut_paseos', models.BooleanField(default=False)),
                ('aut_medica', models.BooleanField(default=False)),
                ('aut_salida', models.BooleanField(default=False)),
                ('aut_publica', models.BooleanField(default=False)),
            ],
            bases=('administracion.persona',),
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='administracion.persona')),
                ('cuil', models.CharField(blank=True, max_length=15, null=True)),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=10)),
                ('fecha_antiguedad', models.DateField(blank=True, null=True)),
                ('antiguedad_reconocida', models.IntegerField(blank=True, null=True)),
                ('estadistica', models.CharField(choices=[('En actividad', 'En actividad'), ('Tareas pasivas', 'Tareas pasivas'), ('Docentes afectados al JIF pero de otra POF', 'Docentes afectados al JIF pero de otra POF'), ('Docentes del JIF afectados a otro establecimiento', 'Docentes del JIF afectados a otro establecimiento'), ('Sin subvención', 'Sin subvención'), ('Baja', 'Baja'), ('Fuera de actividad', 'InaFuera de actividadctivo'), ('A.T. / Integrador', 'A.T. / Integrador'), ('Par pedagógico / Dep. de dirección privada', 'Par pedagógico / Dep. de dirección privada')], default='En actividad', max_length=50)),
            ],
            bases=('administracion.persona',),
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='administracion.persona')),
                ('Profesion', models.CharField(blank=True, max_length=15, null=True)),
                ('domicilio_laboral', models.CharField(blank=True, max_length=30, null=True)),
                ('telefono_laboral', models.CharField(blank=True, max_length=12, null=True)),
            ],
            bases=('administracion.persona',),
        ),
        migrations.AddField(
            model_name='persona',
            name='rol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.rol'),
        ),
    ]
