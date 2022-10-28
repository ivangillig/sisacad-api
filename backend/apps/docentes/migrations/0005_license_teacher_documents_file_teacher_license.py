# Generated by Django 4.1.2 on 2022-10-27 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('docentes', '0004_position_teacher_delete_motive'),
    ]

    operations = [
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_type', models.CharField(blank=True, max_length=30, null=True, unique=True, verbose_name='Tipo de licencia')),
                ('created_date', models.DateField(blank=True, null=True, verbose_name='Fecha de ingreso')),
            ],
            options={
                'verbose_name': 'Licencia',
                'verbose_name_plural': 'Licencias',
            },
        ),
        migrations.AddField(
            model_name='teacher_documents',
            name='file',
            field=models.FileField(null=True, upload_to='documentos/alumnos/%Y', verbose_name='Documento'),
        ),
        migrations.CreateModel(
            name='Teacher_License',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to='documentos/licencias', verbose_name='Documento')),
                ('created_date', models.DateField(blank=True, null=True, verbose_name='Fecha de ingreso')),
                ('is_paid', models.BooleanField(default=False, max_length=150, verbose_name='Con goce')),
                ('license_from', models.DateField(blank=True, null=True, verbose_name='Licencia desde')),
                ('license_to', models.DateField(blank=True, null=True, verbose_name='Licencia hasta')),
                ('license', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docentes.license', verbose_name='Licencia')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='docentes.teacher', verbose_name='Docente')),
            ],
            options={
                'verbose_name': 'Docente_Licencia',
                'verbose_name_plural': 'Docentes_Licencias',
            },
        ),
    ]
