# Generated by Django 4.1.2 on 2022-10-27 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0002_withdraw_authorized_student_withdraw_authorized_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='withdraw_authorized',
            name='student',
        ),
        migrations.AlterField(
            model_name='withdraw_authorized',
            name='doc_number',
            field=models.CharField(max_length=15, primary_key=True, serialize=False, unique=True, verbose_name='DNI'),
        ),
    ]
