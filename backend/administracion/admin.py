from django.contrib import admin

# Importo los modelos
from administracion.models import Persona, Docente, Materia, Alumno, Documentacion_Docente, Rol, Tutor, Tutor_Alumno, Division, Nivel, Modalidad, Año, Curso, Curso_Alumno

# Register your models here.
admin.site.register(Persona)
admin.site.register(Documentacion_Docente)
admin.site.register(Docente)
admin.site.register(Alumno)
admin.site.register(Rol)
admin.site.register(Tutor)
admin.site.register(Tutor_Alumno)
admin.site.register(Division)
admin.site.register(Nivel)
admin.site.register(Modalidad)
admin.site.register(Año)
admin.site.register(Curso)
admin.site.register(Curso_Alumno)
admin.site.register(Materia)

# class ComentarioInline(admin.TabularInline):
#     model = Comentario

# class PostAdmin(admin.ModelAdmin):
#     inlines = [
#         ComentarioInline,
#     ]

# admin.site.register(Post, PostAdmin)