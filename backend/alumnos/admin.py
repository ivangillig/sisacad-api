from django.contrib import admin

# Importo los modelos
from alumnos.models import Alumno, Tutor, Tutor_Alumno

# Register your models here.
admin.site.register(Alumno)
admin.site.register(Tutor)
admin.site.register(Tutor_Alumno)
