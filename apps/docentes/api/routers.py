"""rest URL Configuration"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import BankAccountViewSet
from apps.docentes.api.api import bank_account_detail_view

router = DefaultRouter()

router.register(r'secretaria/docente/cuenta_banco', BankAccountViewSet, basename='bank-accounts')
#router.register(r'secretaria/docente/cuenta_banco/<int:pk>', bank_account_detail_view, basename='api_cuenta_bancaria'),

urlpatterns = [
    path('', include(router.urls)),
]
