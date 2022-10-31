from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.docentes.api.serializers.serializer import *
from apps.docentes.models import *

# class LicenseAPIView(APIView):

#     def get(self, request):
#         license = License.objects.all()
#         license_serializer = LicenseSerializer(license, many=True)
#         return Response(license_serializer.data)

@api_view(['GET', 'POST'])
def bank_account_api_view(request):

    # list
    if request.method == 'GET':
        # queryset
        bank_accounts = Bank_Account.objects.all().values('id', 'cbu', 'teacher')
        bank_account_serializer = Bank_AccountSerializer(bank_accounts, many=True)

        return Response(bank_account_serializer.data, status = status.HTTP_200_OK)

    # create
    elif request.method == 'POST':
        bank_account_serializer = Bank_AccountSerializer(data = request.data)

        # validation
        if bank_account_serializer.is_valid():
            bank_account_serializer.save()
            return Response({'message': 'Cuenta bancaria creada correctamente!'}, status = status.HTTP_201_CREATED)
        return Response(bank_account_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def bank_account_detail_view(request, pk):

    # queryset
    bank_account = Bank_Account.objects.filter(id = pk).first()
    
    # validation
    if bank_account:
        
        #retrieve
        if request.method == 'GET':
            bank_account_serializer = Bank_AccountSerializer(bank_account)
            return Response(bank_account_serializer.data, status = status.HTTP_200_OK)

        #update
        elif request.method == 'PUT':
            bank_account_serializer = Bank_AccountSerializer(bank_account, data = request.data)
            if bank_account_serializer.is_valid():
                bank_account_serializer.save()
                return Response(bank_account_serializer.data, status = status.HTTP_200_OK)
            return Response(bank_account_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        #delete
        elif request.method =='DELETE':
            bank_account = Bank_Account.objects.filter(id = pk).first()
            bank_account.delete()
            return Response({'message': 'Cuenta eliminada correctamente!'}, status = status.HTTP_200_OK)

    return Response({'message': 'No se ha encontrado una cuenta con estos datos'}, status = status.HTTP_400_BAD_REQUEST)