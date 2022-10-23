# Generated by Django 4.1.2 on 2022-10-23 15:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('administracion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='documentacion_docente',
            name='documentacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.documentacion'),
        ),
        migrations.AddField(
            model_name='curso_alumno',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.curso'),
        ),
        migrations.AddField(
            model_name='curso',
            name='año',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.año'),
        ),
        migrations.AddField(
            model_name='año',
            name='division',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.division'),
        ),
        migrations.AddField(
            model_name='año',
            name='modalidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.modalidad'),
        ),
        migrations.AddField(
            model_name='año',
            name='nivel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.nivel'),
        ),
        migrations.AddField(
            model_name='tutor_alumno',
            name='alumno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.alumno'),
        ),
        migrations.AddField(
            model_name='tutor_alumno',
            name='tutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.tutor'),
        ),
        migrations.AddField(
            model_name='nivel',
            name='docente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='docente', to='administracion.docente'),
        ),
        migrations.AddField(
            model_name='documentacion_docente',
            name='docente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.docente'),
        ),
        migrations.AddField(
            model_name='curso_alumno',
            name='alumno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.alumno'),
        ),
        migrations.AddConstraint(
            model_name='curso',
            constraint=models.UniqueConstraint(fields=('año', 'año_lectivo'), name='id_curso_combinacion'),
        ),
        migrations.AddConstraint(
            model_name='tutor_alumno',
            constraint=models.UniqueConstraint(fields=('tutor', 'alumno'), name='tutor_alumno_combinacion'),
        ),
        migrations.AddConstraint(
            model_name='curso_alumno',
            constraint=models.UniqueConstraint(fields=('curso', 'alumno'), name='curso_alumno_combinacion'),
        ),
    ]
