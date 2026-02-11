from rest_framework import viewsets

from .models import Clinica, Tutor , Profissional

from .serializers import (
    ClinicaSerializer,
    TutorSerializer,
    ProfissionalSerializer
)

# rotas para a clinica
class ClinicaViewSet(viewsets.ModelViewSet):
    queryset = Clinica.objects.prefetch_related(
        "tutores__pets__vacinacoes__vacina"
    )
    serializer_class = ClinicaSerializer

#rotas para o tutor
class TutorViewSet(viewsets.ModelViewSet):
    queryset = Tutor.objects.prefetch_related(
        "pets__vacinacoes__vacina"
    )
    serializer_class = TutorSerializer

#rotas para o profissional
class ProfissionalViewSet(viewsets.ModelViewSet):
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer