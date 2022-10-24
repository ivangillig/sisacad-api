""" rest URL Configuration """


from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('administracion.urls')),
    path('', include('alumnos.urls')),
]
