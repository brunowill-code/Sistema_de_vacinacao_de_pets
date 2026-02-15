from rest_framework import serializers
from clinic.models.tutor_model import Tutor
from pets.serializers.pets_serializer import PetsSerializer



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