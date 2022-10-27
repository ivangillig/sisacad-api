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



admin.site.register(Withdraw_Authorized)

class Student_Withdraw_AuthorizedAdmin(admin.ModelAdmin):
    model = Student, Withdraw_Authorized

    list_display = ('id', 'student', 'withdraw_authorized', 'relationship')
    
    def withdraw_authorized(self,obj):
        return obj.withdraw_authorized.name + ' ' + obj.withdraw_authorized.lastname 

    def student(self,obj):
        return obj.student.first_name + ' ' + obj.student.first_lastname 

admin.site.register(Student_Withdraw_Authorized, Student_Withdraw_AuthorizedAdmin)

admin.site.register(Payment)

class Payment_StudentAdmin(admin.ModelAdmin):
    model = Student, Payment

    list_display = ('id', 'payment_id', 'payment_type', 'student')
    
    def payment_id(self,obj):
        return obj.payment.id
    
    def payment_type(self,obj):
        return obj.payment.payment_type 

    def student(self,obj):
        return obj.student.first_name + ' ' + obj.student.first_lastname 


admin.site.register(Payment_Student, Payment_StudentAdmin)

admin.site.register(Student_Documents)