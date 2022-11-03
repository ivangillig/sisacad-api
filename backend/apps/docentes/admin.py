from django.contrib import admin

# Register your models here.
from apps.docentes.models import *
from apps.administracion.models import Bank, Documents
from simple_history.admin import SimpleHistoryAdmin

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'doc_number', 'first_lastname', 'first_name')


admin.site.register(Teacher, TeacherAdmin)

class Teacher_DocumentsAdmin(admin.ModelAdmin):
    model = Teacher, Documents

    list_display = ( 'teacher', 'documents', 'file', 'created_date')

    def teacher(self,obj):
        return obj.teacher

    def documents(self,obj):
        return obj.documents


admin.site.register(Teacher_Documents, Teacher_DocumentsAdmin)
admin.site.register(Salary_Receipt)

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


class DisponibilityHistoryAdmin (SimpleHistoryAdmin):
    list_display = ['teacher', 'state', 'init_time', 'end_time']
    history_list_display = ['state']

    def teacher(self,obj):
        return obj.teacher

admin.site.register(Disponibility, DisponibilityHistoryAdmin)