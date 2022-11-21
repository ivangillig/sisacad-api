from django.urls import path
from apps.docentes.api.api import bank_account_api_view, bank_account_detail_view
urlpatterns = [
    #path(r'api/docente/licencia', LicenseAPIView.as_view(), name = 'api_docentes_licencias'),
    path(r'secretaria/docente/cuenta_banco', bank_account_api_view, name = 'api_cuentas_bancarias'),
    path(r'secretaria/docente/cuenta_banco/<int:pk>', bank_account_detail_view, name = 'api_cuenta_bancaria'),
]
