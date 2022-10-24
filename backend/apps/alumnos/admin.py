from django.contrib import admin

# Importo los modelos
from apps.alumnos.models import Student, Student_Tutor, Tutor

# Register your models here.
admin.site.register(Student)
admin.site.register(Tutor)
admin.site.register(Student_Tutor)
