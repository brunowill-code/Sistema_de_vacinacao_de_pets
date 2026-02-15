from rest_framework import serializers

from clinic.models.profissional_model import Profissional


class ProfissionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profissional
        fields = ["id", "nome", "crmv"]