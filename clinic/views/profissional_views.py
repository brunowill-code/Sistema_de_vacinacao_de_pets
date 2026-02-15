from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated


from clinic.models.profissional_model import Profissional
from setup.permissions import IsClinicOwner

from clinic.serializers.profissional_serializer import ProfissionalSerializer

#rotas para o profissional
class ProfissionalViewSet(viewsets.ModelViewSet):
    serializer_class = ProfissionalSerializer
    permission_classes = [IsAuthenticated, IsClinicOwner]

    def get_queryset(self):
        return Profissional.objects.filter(
            clinica=self.request.user.clinica
        )

    def perform_create(self, serializer):
        serializer.save(
            clinica=self.request.user.clinica
        )