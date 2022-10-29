from rest_framework import serializers
from apps.docentes.models import License, Bank_Account

class LicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = License
        fields = '__all__'

class Bank_AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank_Account
        fields = '__all__'