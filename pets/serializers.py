from rest_framework import serializers

from vaccines.serializers import VacinacaoSerializer
from .models import Pets

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
