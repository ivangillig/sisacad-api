from django.contrib import admin

# Importo los modelos
from apps.administracion.models import *
from apps.users.models import Person, Role
from apps.docentes.models import *

# Register your models here.
admin.site.register(Person)
admin.site.register(Teacher)
admin.site.register(Teacher_Documents)
admin.site.register(Role)
admin.site.register(Division)
admin.site.register(Level)
admin.site.register(Speciality)
admin.site.register(Grade)
admin.site.register(Course)
admin.site.register(Course_Student)
admin.site.register(Subject)

