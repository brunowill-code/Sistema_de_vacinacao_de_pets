from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated

from .models import Clinica, Tutor , Profissional

from setup.permissions import IsClinicOwner

from .serializers import (
    ClinicaSerializer,
    TutorSerializer,
    ProfissionalSerializer
)

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
    

#rotas para o tutor
class TutorViewSet(viewsets.ModelViewSet):
    serializer_class = TutorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Tutor.objects.filter(
            clinica=self.request.user.clinica
        ).prefetch_related(
            "pets__vacinacoes__vacina"
        )

    def perform_create(self, serializer):
        serializer.save(
            clinica=self.request.user.clinica
        )

#rotas para o profissional
class ProfissionalViewSet(viewsets.ModelViewSet):
    serializer_class = ProfissionalSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Profissional.objects.filter(
            clinica=self.request.user.clinica
        )

    def perform_create(self, serializer):
        serializer.save(
            clinica=self.request.user.clinica
        )