# Generated by Django 4.2.1 on 2023-08-14 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docentes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank_account',
            name='deleted_date',
            field=models.DateField(null=True, verbose_name='Fecha de eliminación'),
        ),
        migrations.AlterField(
            model_name='degree',
            name='deleted_date',
            field=models.DateField(null=True, verbose_name='Fecha de eliminación'),
        ),
        migrations.AlterField(
            model_name='disponibility',
            name='deleted_date',
            field=models.DateField(null=True, verbose_name='Fecha de eliminación'),
        ),
        migrations.AlterField(
            model_name='historicaldisponibility',
            name='deleted_date',
            field=models.DateField(null=True, verbose_name='Fecha de eliminación'),
        ),
        migrations.AlterField(
            model_name='license',
            name='deleted_date',
            field=models.DateField(null=True, verbose_name='Fecha de eliminación'),
        ),
        migrations.AlterField(
            model_name='permission_request',
            name='deleted_date',
            field=models.DateField(null=True, verbose_name='Fecha de eliminación'),
        ),
        migrations.AlterField(
            model_name='salary_receipt',
            name='deleted_date',
            field=models.DateField(null=True, verbose_name='Fecha de eliminación'),
        ),
        migrations.AlterField(
            model_name='teacher_degree',
            name='deleted_date',
            field=models.DateField(null=True, verbose_name='Fecha de eliminación'),
        ),
        migrations.AlterField(
            model_name='teacher_documents',
            name='deleted_date',
            field=models.DateField(null=True, verbose_name='Fecha de eliminación'),
        ),
        migrations.AlterField(
            model_name='teacher_license',
            name='deleted_date',
            field=models.DateField(null=True, verbose_name='Fecha de eliminación'),
        ),
    ]