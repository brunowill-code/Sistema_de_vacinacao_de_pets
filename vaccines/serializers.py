from rest_framework import serializers

from .models import Vacina , Vacinacao

from clinic.models import Profissional


class ProfissionalNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profissional
        fields = ["id", "nome"]

class VacinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacina
        fields = ["id", "nome", "descricao", "fabricante"]

class VacinacaoSerializer(serializers.ModelSerializer):
    vacina = VacinaSerializer(read_only=True)
    profissional = ProfissionalNestedSerializer(read_only=True)

    class Meta:
        model = Vacinacao
        fields = [
            "id",
            "vacina",
            "data_aplicacao",
            "proxima_dose",
            "observacoes",
            "profissional"
        ]