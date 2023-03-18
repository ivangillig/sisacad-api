from rest_framework import serializers
from apps.docentes.models import License, Bank_Account

class LicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = License
        fields = '__all__'

class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank_Account
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'cbu': instance['cbu'],
            'teacher': instance['teacher'],
            } 