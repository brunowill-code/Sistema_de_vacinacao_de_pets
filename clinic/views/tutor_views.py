from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated


from clinic.models.tutor_model import Tutor
from setup.permissions import IsClinicOwner

from clinic.serializers.tutor_serializer import TutorSerializer


class TutorViewSet(viewsets.ModelViewSet):
    serializer_class = TutorSerializer
    permission_classes = [IsAuthenticated, IsClinicOwner]

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