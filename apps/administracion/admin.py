from django.contrib import admin

# Importo los modelos
from apps.administracion.models import *


admin.site.register(Documents)

class PositionAdmin(admin.ModelAdmin):
    model = Category

    list_display = ( 'id', 'cat_name', 'place_number1', 'place_number2', 'hours_qty')
    
    def cat_name(self,obj):
        return obj.category.name

admin.site.register(Position, PositionAdmin)
class GradeAdmin(admin.ModelAdmin):
    model = Category

    list_display = ( 'id', 'name', 'level_name', 'division_name') #'speciality_name' - Ver ternario para los las modalidades nulas)
    
    def level_name(self,obj):
        return obj.level.name
    def division_name(self,obj):
        return obj.division.name 

admin.site.register(Grade, GradeAdmin)
admin.site.register(Division)
admin.site.register(Level)
admin.site.register(Speciality)

class CourseAdmin(admin.ModelAdmin):
    model = Category

    list_display = ( 'grade_name', 'level_name', 'division_name', 'academic_year')
    
    def level_name(self,obj):
        return obj.grade.level.name
    def division_name(self,obj):
        return obj.grade.division.name 
    def grade_name(self,obj):
        return obj.grade.name

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


admin.site.register(Course_Subject)
admin.site.register(Course, CourseAdmin)
admin.site.register(Course_Student)
admin.site.register(Subject)
admin.site.register(Category)
admin.site.register(Bank)

