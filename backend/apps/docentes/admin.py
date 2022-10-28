from django.contrib import admin

# Register your models here.
from apps.docentes.models import *
from apps.administracion.models import Bank, Position

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('doc_number', 'first_lastname', 'first_name')


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Teacher_Documents)
admin.site.register(Salary_Receipt)

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

admin.site.register(License)

class Teacher_LicenseAdmin(admin.ModelAdmin):
    model = Teacher, License

    list_display = ( 'teacher', 'license', 'license_from', 'license_to')

    def teacher(self,obj):
        return obj.teacher

    def license(self,obj):
        return obj.license


class Bank_AccountAdmin(admin.ModelAdmin):
    model = Teacher, Bank

    list_display = ( 'teacher', 'bank', 'cbu')

    def teacher(self,obj):
        return obj.teacher

    def bank(self,obj):
        return obj.bank

admin.site.register(Bank_Account, Bank_AccountAdmin)

admin.site.register(Permission_Request)
admin.site.register(Degree)

class Teacher_DegreeAdmin(admin.ModelAdmin):
    model = Teacher, Degree

    list_display = ( 'teacher', 'degree', 'institucion_degree', 'graduated_date')

    def teacher(self,obj):
        return obj.teacher

    def degree(self,obj):
        return obj.degree

    def graduated_date(self,obj):
        return obj.graduated_date

    def institucion_degree(self,obj):
        return obj.institution

admin.site.register(Teacher_Degree, Teacher_DegreeAdmin)