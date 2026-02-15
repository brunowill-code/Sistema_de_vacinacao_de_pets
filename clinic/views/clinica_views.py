from rest_framework.exceptions import ValidationError
from rest_framework import viewsets
from rest_framework import status

from rest_framework.response import Response


from rest_framework.permissions import IsAuthenticated, IsAdminUser

from clinic.models.clinica_model import Clinica
from setup.permissions import IsClinicOwner

from clinic.serializers.clinica_serializer import ClinicaSerializer

# rotas para a clinica
class ClinicaViewSet(viewsets.ModelViewSet):
    serializer_class = ClinicaSerializer
    permission_classes = [IsAuthenticated, IsClinicOwner]

    def get_queryset(self):
        return Clinica.objects.filter(
            owner=self.request.user
        ).prefetch_related(
            "tutores__pets__vacinacoes__vacina"
        )

    def perform_create(self, serializer):

        user = self.request.user
        if Clinica.objects.filter(owner=user).exists():
            raise ValidationError(
                {"message": "Um owner pode possuir apenas uma clínica"}
            )

        serializer.save(owner=self.request.user)
    