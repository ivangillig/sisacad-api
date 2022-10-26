from django.contrib import admin

# Importo los modelos
from apps.alumnos.models import *

class StudentAdmin(admin.ModelAdmin):
    list_display = ('doc_number', 'first_name', 'first_lastname')

# Register your models here.
admin.site.register(Student, StudentAdmin)
admin.site.register(Tutor)
admin.site.register(Student_Tutor)
