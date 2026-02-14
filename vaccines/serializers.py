from rest_framework import serializers

from .models import Vacina , Vacinacao

from clinic.models import Profissional

from pets.models import Pets


class ProfissionalNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profissional
        fields = ["id", "nome", "crmv"]

class VacinaSerializer(serializers.ModelSerializer):

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

class VacinacaoSerializer(serializers.ModelSerializer):

    # =========================
    # CAMPOS PARA ESCRITA (POST)
    # =========================
    vacina = serializers.PrimaryKeyRelatedField(
        queryset=Vacina.objects.all()
    )

    profissional = serializers.PrimaryKeyRelatedField(
        queryset=Profissional.objects.all()
    )

    pet = serializers.PrimaryKeyRelatedField(
        queryset=Pets.objects.all()
    )

    # =========================
    # CAMPOS PARA LEITURA (GET)
    # =========================
    vacina_detalhe = VacinaSerializer(
        source="vacina",
        read_only=True
    )

    profissional_detalhe = ProfissionalNestedSerializer(
        source="profissional",
        read_only=True
    )

    class Meta:
        model = Vacinacao
        fields = [
            "id",
            "pet",
            "vacina",
            "profissional",
            "vacina_detalhe",
            "profissional_detalhe",
            "proxima_dose",
            "observacoes",
        ]

    # =========================
    # FILTRA QUERYSETS POR CLÍNICA
    # =========================
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        request = self.context.get("request")

        if request and request.user.is_authenticated:
            clinica = request.user.clinica

            self.fields["pet"].queryset = Pets.objects.filter(
                clinica=clinica
            )

            self.fields["vacina"].queryset = Vacina.objects.filter(
                clinica=clinica
            )

            self.fields["profissional"].queryset = Profissional.objects.filter(
                clinica=clinica
            )

    # =========================
    # VALIDAÇÃO EXTRA DE SEGURANÇA
    # =========================
    def validate(self, data):
        request = self.context["request"]
        clinica_usuario = request.user.clinica

        if data["pet"].clinica != clinica_usuario:
            raise serializers.ValidationError(
                {"pet": "Este pet não pertence à sua clínica."}
            )

        if data["vacina"].clinica != clinica_usuario:
            raise serializers.ValidationError(
                {"vacina": "Esta vacina não pertence à sua clínica."}
            )

        if data["profissional"].clinica != clinica_usuario:
            raise serializers.ValidationError(
                {"profissional": "Este profissional não pertence à sua clínica."}
            )

        return data