# Generated by Django 4.1.2 on 2022-10-24 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0004_alter_division_state_alter_grade_division_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='division',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administracion.division', verbose_name='División'),
        ),
        migrations.AlterField(
            model_name='grade',
            name='speciality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administracion.speciality', verbose_name='Modalidad'),
        ),
    ]