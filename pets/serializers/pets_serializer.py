from rest_framework import serializers

from vaccines.serializers.vacinacao_serializer import VacinacaoSerializer
from ..models.pets_model import Pets

class PetsSerializer(serializers.ModelSerializer):
    vacinacoes = VacinacaoSerializer(many=True, read_only=True)

    class Meta:
        model = Pets
        fields = [
            "id",
            "nome",
            "especie",
            "raca",
            "sexo",
            "data_de_nascimento",
            "peso",
            "vacinacoes"
        ]
