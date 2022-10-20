# Generated by Django 4.1.2 on 2022-10-18 20:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Año',
            fields=[
                ('id_año', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=30, null=True)),
                ('estado', models.CharField(blank=True, choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=8, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id_division', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=15, null=True)),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=8, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Documentacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_documentacion', models.CharField(choices=[('DNI', 'DNI'), ('Certificado', 'Certificado'), ('Constancia 1', 'Constancia 1'), ('Constancia 2', 'Constancia 2')], default='DNI', max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Modalidad',
            fields=[
                ('id_modalidad', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=30, null=True)),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=8, null=True)),
                ('fecha_alta', models.DateField(blank=True, null=True)),
                ('fecha_baja', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nivel',
            fields=[
                ('id_nivel', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=30, null=True)),
                ('estado', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=8, null=True)),
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
                ('dni', models.CharField(blank=True, max_length=13, null=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('lugar_nacimiento', models.CharField(blank=True, max_length=15, null=True)),
                ('nacionalidad', models.CharField(blank=True, max_length=15, null=True)),
                ('genero', models.CharField(blank=True, choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Sin_Genero', 'X')], default='Masculino', max_length=20, null=True)),
                ('direccion', models.CharField(blank=True, max_length=15, null=True)),
                ('barrio', models.CharField(blank=True, max_length=15, null=True)),
                ('telefono', models.CharField(blank=True, max_length=15, null=True)),
                ('estado_civil', models.CharField(blank=True, choices=[('Soltero', 'Soltero'), ('Casado', 'Casado'), ('Divorciado', 'Divorciado'), ('Viudo/a', 'Viudo/a'), ('No aplica', 'No aplica')], default='No aplica', max_length=20, null=True)),
                ('fecha_alta', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id_post', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=30)),
                ('resumen', models.CharField(max_length=50)),
                ('contenido', models.TextField(max_length=100)),
                ('image', models.ImageField(upload_to='uploads/')),
                ('status', models.CharField(choices=[('Publicado', 'Publicado'), ('Borrador', 'Borrador')], default='Borrador', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id_rol', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(choices=[('Madre', 'Madre'), ('Padre', 'Padre'), ('Tutor legal', 'Tutor legal')], default='Madre', max_length=15, null=True)),
                ('Profesion', models.CharField(max_length=15)),
                ('domicilio_laboral', models.CharField(max_length=30)),
                ('telefono_laboral', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='administracion.persona')),
                ('cuil', models.CharField(blank=True, max_length=15, null=True)),
                ('estado', models.CharField(blank=True, choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], default='Activo', max_length=10, null=True)),
                ('email_institucional', models.EmailField(blank=True, max_length=40, null=True)),
                ('fecha_antiguedad', models.DateField(blank=True, null=True)),
                ('antiguedad_reconocida', models.IntegerField(blank=True, null=True)),
                ('estadistica', models.CharField(blank=True, choices=[('En actividad', 'En actividad'), ('Tareas pasivas', 'Tareas pasivas'), ('Docentes afectados al JIF pero de otra POF', 'Docentes afectados al JIF pero de otra POF'), ('Docentes del JIF afectados a otro establecimiento', 'Docentes del JIF afectados a otro establecimiento'), ('Sin subvención', 'Sin subvención'), ('Baja', 'Baja'), ('Fuera de actividad', 'InaFuera de actividadctivo'), ('A.T. / Integrador', 'A.T. / Integrador'), ('Par pedagógico / Dep. de dirección privada', 'Par pedagógico / Dep. de dirección privada')], default='En actividad', max_length=50, null=True)),
            ],
            bases=('administracion.persona',),
        ),
        migrations.AddField(
            model_name='persona',
            name='id_rol',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administracion.rol'),
        ),
        migrations.AddField(
            model_name='persona',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('año_lectivo', models.IntegerField(blank=True, null=True)),
                ('turno', models.CharField(blank=True, choices=[('Mañana', 'Mañana'), ('Tarde', 'Tarde'), ('Noche', 'Noche')], default='Mañana', max_length=8, null=True)),
                ('año', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administracion.año')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id_comentario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('comentario', models.TextField()),
                ('email', models.EmailField(max_length=40)),
                ('status', models.CharField(choices=[('Publicado', 'Publicado'), ('Borrador', 'Borrador')], default='Borrador', max_length=20)),
                ('fecha_creado', models.DateField()),
                ('id_post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administracion.post')),
            ],
        ),
        migrations.AddField(
            model_name='año',
            name='id_division',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administracion.division'),
        ),
        migrations.AddField(
            model_name='año',
            name='id_modalidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administracion.modalidad'),
        ),
        migrations.AddField(
            model_name='año',
            name='id_nivel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administracion.nivel'),
        ),
        migrations.CreateModel(
            name='Documentacion_Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ruta_archivo', models.CharField(blank=True, max_length=30, null=True)),
                ('fecha_ingreso', models.DateField(blank=True, null=True)),
                ('documentacion_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administracion.documentacion')),
                ('docente_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administracion.docente')),
            ],
        ),
        migrations.AddConstraint(
            model_name='curso',
            constraint=models.UniqueConstraint(fields=('año', 'año_lectivo'), name='id_curso_combinacion'),
        ),
    ]
