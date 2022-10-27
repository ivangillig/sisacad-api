from django.contrib import admin

# Importo los modelos
from apps.alumnos.models import *

class StudentAdmin(admin.ModelAdmin):
    list_display = ('doc_number', 'first_name', 'first_lastname')

class Student_TutorAdmin(admin.ModelAdmin):
    model = Tutor, Student

    list_display = ('student', 'tutor','relationship')
    
    def tutor(self,obj):
        return obj.Tutor.first_name

    def student(self,obj):
        return obj.Student.first_name

admin.site.register(Student, StudentAdmin)
admin.site.register(Tutor)
admin.site.register(Student_Tutor, Student_TutorAdmin)
