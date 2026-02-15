from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'password', 'telefone', 'cnpj']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.Meta.model = get_user_model()

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)