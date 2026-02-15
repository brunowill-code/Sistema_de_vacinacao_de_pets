from rest_framework import viewsets
from setup.permissions import IsClinicOwner
from rest_framework.permissions import IsAuthenticated

from vaccines.models.vacinacao_model import Vacina
from vaccines.serializers.vacinacao_serializer import VacinaSerializer


#Rotas para as Vacinas
class VacinaViewSet(viewsets.ModelViewSet):
    serializer_class = VacinaSerializer
    permission_classes = [IsAuthenticated, IsClinicOwner]

    def get_queryset(self):
        return Vacina.objects.filter(
            clinica=self.request.user.clinica
        )

    def perform_create(self, serializer):
        serializer.save(
            clinica=self.request.user.clinica
        )