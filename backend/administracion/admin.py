from django.contrib import admin

# Importo los modelos
from administracion.models import Persona, Docente, Materia, Alumno, Documentacion_Docente, Rol, Tutor, Comentario, Post, Division, Nivel, Modalidad, Año, Curso, CursoAlumnos

# Register your models here.
admin.site.register(Persona)
admin.site.register(Documentacion_Docente)
admin.site.register(Docente)
admin.site.register(Alumno)
admin.site.register(Rol)
admin.site.register(Tutor)
admin.site.register(Division)
admin.site.register(Nivel)
admin.site.register(Modalidad)
admin.site.register(Año)
admin.site.register(Curso)
admin.site.register(CursoAlumnos)
admin.site.register(Materia)

#admin.site.register(Categoria)
#admin.site.register(Comentario)

class ComentarioInline(admin.TabularInline):
    model = Comentario

class PostAdmin(admin.ModelAdmin):
    inlines = [
        ComentarioInline,
    ]

admin.site.register(Post, PostAdmin)