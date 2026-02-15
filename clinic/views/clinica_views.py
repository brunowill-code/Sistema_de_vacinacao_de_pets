from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated


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
        serializer.save(owner=self.request.user)
    