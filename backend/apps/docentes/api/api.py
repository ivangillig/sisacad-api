from urllib import request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.docentes.api.serializer import *
from apps.docentes.models import *

# class LicenseAPIView(APIView):

#     def get(self, request):
#         license = License.objects.all()
#         license_serializer = LicenseSerializer(license, many=True)
#         return Response(license_serializer.data)

@api_view(['GET', 'POST'])
def bank_account_api_view(request):

    if request.method == 'GET':
        bank_accounts = Bank_Account.objects.all()
        bank_account_serializer = Bank_AccountSerializer(bank_accounts, many=True)
        return Response(bank_account_serializer.data)

    elif request.method == 'POST':
        bank_account_serializer = Bank_AccountSerializer(data = request.data)
        if bank_account_serializer.is_valid():
            bank_account_serializer.save()
            return Response(bank_account_serializer.data)
        return Response(bank_account_serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def bank_account_detail_view(request, pk):

    if request.method == 'GET':
        bank_account = Bank_Account.objects.filter(id = pk).first()
        bank_account_serializer = Bank_AccountSerializer(bank_account)
        return Response(bank_account_serializer.data)

    elif request.method == 'PUT':
        bank_account = Bank_Account.objects.filter(id = pk).first()
        bank_account_serializer = Bank_AccountSerializer(bank_account, data = request.data)
        if bank_account_serializer.is_valid():
            bank_account_serializer.save()
            return Response(bank_account_serializer.data)
        return Response(bank_account_serializer.errors)
    
    elif request.method =='DELETE':
        bank_account = Bank_Account.objects.filter(id = pk).first()
        bank_account.delete()
        return Response('Cuenta bancaria eliminada')