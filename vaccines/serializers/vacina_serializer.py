from rest_framework import serializers

from clinic.models.profissional_model import Profissional

from vaccines.models.vacinacao_model import Vacina

class VacinaSerializer(serializers.ModelSerializer):

    clinica = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Vacina
        fields = [
            "id",
            "clinica",
            "nome",
            "fabricante",
            "lote",
            "data_fabricacao",
            "data_validade",
            "descricao",
            "especie_indicada",
            "intervalo_doses_dias",
            "quantidade_estoque",
        ]
        read_only_fields = ["clinica"]

    def validate(self, data):
        """
        Validação para garantir que a data de validade
        seja maior que a data de fabricação.
        """
        if data["data_validade"] <= data["data_fabricacao"]:
            raise serializers.ValidationError(
                "A data de validade deve ser maior que a data de fabricação."
            )

        if data["quantidade_estoque"] < 0:
            raise serializers.ValidationError(
                "A quantidade em estoque não pode ser negativa."
            )

        if data["intervalo_doses_dias"] <= 0:
            raise serializers.ValidationError(
                "O intervalo entre doses deve ser maior que zero."
            )

        return data