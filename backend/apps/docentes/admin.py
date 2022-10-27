from django.contrib import admin

# Register your models here.
from apps.docentes.models import *
from apps.administracion.models import Position

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('doc_number', 'first_lastname', 'first_name')


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Teacher_Documents)

class Position_TeacherAdmin(admin.ModelAdmin):
    model = Position

    list_display = ( 'place_number1', 'category_name', 'category_id', 'teacher_name', 'teacher_lastname', 'position_type')

    def place_number1(self,obj):
        return obj.position.place_number1
        
    place_number1.short_description = 'Nro Plaza'

    def category_id(self,obj):
        return obj.position.category.category_id 

    category_id.short_description = 'Categoría'

    def category_name(self,obj):
        return obj.position.category.name

    category_name.short_description = 'Nombre Categoría'

    def teacher_name(self,obj):
        return obj.teacher.first_name 

    teacher_name.short_description = 'Nombre Docente'

    def teacher_lastname(self,obj):
        return obj.teacher.first_lastname 

    teacher_lastname.short_description = 'Apellido Docente'

admin.site.register(Position_Teacher, Position_TeacherAdmin)
