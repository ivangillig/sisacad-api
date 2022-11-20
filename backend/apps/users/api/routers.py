"""rest URL Configuration"""

from django.urls import path,include

from rest_framework.routers import DefaultRouter
from apps.users.api.views.general_views import UserViewset

router = DefaultRouter()

router.register(r'administracion/user', UserViewset, basename = 'usuario')

urlpatterns = router.urls
