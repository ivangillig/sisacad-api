# Generated by Django 4.1.2 on 2022-10-27 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0005_student_documents'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student_documents',
            options={'verbose_name': 'Alumno_Documento', 'verbose_name_plural': 'Alumnos_Documentos'},
        ),
        migrations.AlterField(
            model_name='student',
            name='medical_treatment',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Tratamiento médico'),
        ),
        migrations.AlterField(
            model_name='student_documents',
            name='file',
            field=models.FileField(upload_to='documentos/alumnos/%Y', verbose_name='Documento'),
        ),
        migrations.AlterField(
            model_name='student_documents',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnos.student', verbose_name='Alumno'),
        ),
    ]