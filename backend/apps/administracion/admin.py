from django.contrib import admin

# Importo los modelos
from apps.administracion.models import Course_Student, Person, Teacher, Subject, Teacher_Documents, Role, Division, Level, Speciality, Grade, Course, Course_Student

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

