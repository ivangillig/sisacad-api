from django.contrib import admin

# Importo los modelos
from apps.administracion.models import *

class PositionAdmin(admin.ModelAdmin):
    model = Category

    list_display = ( 'cat_name', 'place_number1', 'place_number2', 'hours_qty')
    
    def cat_name(self,obj):
        return obj.category.name

admin.site.register(Position, PositionAdmin)

class GradeAdmin(admin.ModelAdmin):
    model = Category

    list_display = ( 'id', 'name', 'level_name', 'division_name', 'speciality_name')
    
    def level_name(self,obj):
        return obj.level.name
    def division_name(self,obj):
        return obj.division.name 
    def speciality_name(self,obj):
        return obj.speciality.name

admin.site.register(Grade, GradeAdmin)

# Register your models here.
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


admin.site.register(Course_Subject)

admin.site.register(Course, CourseAdmin)

admin.site.register(Course_Student)
admin.site.register(Subject)

admin.site.register(Category)

