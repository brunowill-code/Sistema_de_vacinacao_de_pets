from rest_framework import serializers
from .models import Clinica, Tutor, Profissional
from pets.serializers import PetsSerializer



class TutorSerializer(serializers.ModelSerializer):
    pets = PetsSerializer(many=True, read_only=True)
    
    class Meta:
        model = Tutor
        fields = [
            "id",
            "nome",
            "telefone",
            "email",
            "data_de_nascimento",
            "cpf",
            "pets"
        ]
class ProfissionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profissional
        fields = ["id", "nome", "crmv"]


class ClinicaSerializer(serializers.ModelSerializer):
    tutores = TutorSerializer(many=True, read_only=True)
    profissional = ProfissionalSerializer(many=True, read_only=True)
    class Meta:
        model = Clinica
        fields = [
            "id",
            "nome",
            "tutores",
            "profissional"
        ]

