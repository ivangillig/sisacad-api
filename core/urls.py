""" rest URL Configuration """

from django.contrib import admin
from django.urls import include, path, re_path
from apps.users.api.routers import router as users_router
from apps.docentes.api.routers import router as docentes_router
from apps.administracion.api.routers import router as administracion_router
from apps.alumnos.api.routers import router as students_router
from apps.users.api.views.general_views import CustomRegisterView
from django.conf import settings
from django.conf.urls.static import static

#Swagger
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
   openapi.Info(
      title="SisAcad - Documentación de API",
      default_version='v0.1',
      description="Documentación Pública de API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="ivan.gillig@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
urlpatterns = [
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('admin/', admin.site.urls),
   path('api/', include(users_router.urls)),
   path('api/', include(students_router.urls)),
   path('api/', include(administracion_router.urls)),
   path('api/', include(docentes_router.urls)),
   path('auth/', include('dj_rest_auth.urls')),
   path('auth/registration/', CustomRegisterView.as_view(), name='custom-register'),

   #path('auth/registration/', include('dj_rest_auth.registration.urls')),
]

# URL definition in order to avoid access to media files
if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
