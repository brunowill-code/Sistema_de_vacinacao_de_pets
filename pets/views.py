from rest_framework import viewsets
from .models import Pets
from clinic.models import Tutor
from rest_framework.permissions import IsAuthenticated
from setup.permissions import IsClinicOwner

from .serializers import PetsSerializer
# Create your views here.

# rotas para os pets
class PetsViewSet(viewsets.ModelViewSet):
    serializer_class = PetsSerializer
    permission_classes = [IsAuthenticated, IsClinicOwner]

    def get_queryset(self):
        return Pets.objects.filter(
            clinica=self.request.user.clinica
        )

    def perform_create(self, serializer):
        tutor_id = self.request.data.get("tutor")

        tutor = Tutor.objects.get(
            id=tutor_id,
            clinica=self.request.user.clinica
        )

        serializer.save(
            clinica=self.request.user.clinica,
            tutor=tutor
        )