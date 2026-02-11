from rest_framework import serializers
from .models import Vacina , Vacinacao

class VacinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacina
        fields = "__all__"

class VacinacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacinacao
        fields = "__all__"