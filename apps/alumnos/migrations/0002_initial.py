# Generated by Django 4.1.3 on 2022-11-18 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administracion', '0001_initial'),
        ('users', '0001_initial'),
        ('alumnos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.person')),
                ('family_phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Teléfono familiar')),
                ('medical_treatment', models.BooleanField(blank=True, default=False, null=True, verbose_name='Tratamiento médico')),
                ('medications', models.TextField(blank=True, max_length=200, null=True, verbose_name='Medicamentos')),
                ('allergies', models.TextField(blank=True, max_length=200, null=True, verbose_name='Alergias')),
                ('observations', models.TextField(blank=True, max_length=200, null=True, verbose_name='Observaciones')),
                ('school_cert_destinty', models.CharField(blank=True, max_length=30, null=True, verbose_name='Destino de certificado escolar')),
                ('admission_date', models.DateField(blank=True, null=True, verbose_name='Fecha de ingreso')),
                ('leaving_date', models.DateField(blank=True, null=True, verbose_name='Fecha de egreso')),
                ('trips_auth', models.BooleanField(default=False, verbose_name='Autorización de paseos')),
                ('medical_auth', models.BooleanField(default=False, verbose_name='Autorización médica')),
                ('leave_auth', models.BooleanField(default=False, verbose_name='Autorización de salida')),
                ('public_auth', models.BooleanField(default=False, verbose_name='Autorización para publicar')),
            ],
            options={
                'verbose_name': 'Alumno',
                'verbose_name_plural': 'Alumnos',
            },
            bases=('users.person',),
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='users.person')),
                ('profession', models.CharField(blank=True, max_length=15, null=True, verbose_name='Profesión')),
                ('job_address', models.CharField(blank=True, max_length=30, null=True, verbose_name='Domicilio laboral')),
                ('job_phone', models.CharField(blank=True, max_length=12, null=True, verbose_name='Teléfono laboral')),
            ],
            options={
                'verbose_name': 'Tutor',
                'verbose_name_plural': 'Tutores',
            },
            bases=('users.person',),
        ),
        migrations.CreateModel(
            name='Withdraw_Authorized',
            fields=[
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de modificación')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de eliminación')),
                ('doc_number', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True, verbose_name='DNI')),
                ('name', models.CharField(blank=True, max_length=15, null=True, verbose_name='Nombre')),
                ('lastname', models.CharField(blank=True, max_length=15, null=True, verbose_name='Apellido')),
                ('phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Teléfono')),
            ],
            options={
                'verbose_name': 'Autorizado',
                'verbose_name_plural': 'Autorizados',
            },
        ),
        migrations.CreateModel(
            name='Student_Withdraw_Authorized',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de modificación')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de eliminación')),
                ('relationship', models.CharField(choices=[('Hermano/a', 'Hermano/a'), ('Primo/a', 'Primo/a'), ('Tío/a', 'Tío/a'), ('Otro', 'Otro')], default='Hermano/a', max_length=15, verbose_name='Vínculo')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnos.student', verbose_name='Alumno')),
                ('withdraw_authorized', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnos.withdraw_authorized', verbose_name='Autorizado a retiro')),
            ],
            options={
                'verbose_name': 'Autorizado_Alumno',
                'verbose_name_plural': 'Autorizados_Alumnos',
            },
        ),
        migrations.CreateModel(
            name='Student_Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de modificación')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de eliminación')),
                ('relationship', models.CharField(choices=[('Madre', 'Madre'), ('Padre', 'Padre'), ('Tutor legal', 'Tutor legal')], default='Tutor legal', max_length=15, verbose_name='Vínculo')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnos.student', verbose_name='Alumno')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnos.tutor')),
            ],
            options={
                'verbose_name': 'Alumno_Tutor',
                'verbose_name_plural': 'Alumnos_Tutores',
            },
        ),
        migrations.CreateModel(
            name='Student_Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de modificación')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de eliminación')),
                ('file', models.FileField(upload_to='documentos/alumnos/%Y', verbose_name='Documento')),
                ('documents', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.documents', verbose_name='Documentación')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnos.student', verbose_name='Alumno')),
            ],
            options={
                'verbose_name': 'Alumno_Documento',
                'verbose_name_plural': 'Alumnos_Documentos',
            },
        ),
        migrations.AddField(
            model_name='payment_student',
            name='payment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnos.payment', verbose_name='Pago'),
        ),
        migrations.AddField(
            model_name='payment_student',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnos.student', verbose_name='Alumno'),
        ),
        migrations.AddConstraint(
            model_name='student_withdraw_authorized',
            constraint=models.UniqueConstraint(fields=('withdraw_authorized', 'student'), name='authorized_student_combination'),
        ),
        migrations.AddConstraint(
            model_name='student_tutor',
            constraint=models.UniqueConstraint(fields=('tutor', 'student'), name='tutor_student_combination'),
        ),
        migrations.AddConstraint(
            model_name='payment_student',
            constraint=models.UniqueConstraint(fields=('payment', 'student'), name='payment_student_combination'),
        ),
    ]