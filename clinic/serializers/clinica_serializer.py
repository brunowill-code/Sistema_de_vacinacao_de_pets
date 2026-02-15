from rest_framework import serializers

from clinic.models.clinica_model import Clinica


from .tutor_serializer import TutorSerializer
from .profissional_serializer import ProfissionalSerializer


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

