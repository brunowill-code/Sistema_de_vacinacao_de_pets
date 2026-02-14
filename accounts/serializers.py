from rest_framework import serializers
from django.contrib.auth import get_user_model
from clinic.models import Clinica

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'password', 'telefone', 'cnpj']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)