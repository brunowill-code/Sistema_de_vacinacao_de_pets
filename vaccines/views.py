from rest_framework import viewsets
from .models import Vacina, Vacinacao
from .serializers import VacinacaoSerializer, VacinaSerializer
from setup.permissions import IsClinicOwner
from rest_framework.permissions import IsAuthenticated


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

#Rotas para as Vacinações
class VacinacaoViewSet(viewsets.ModelViewSet):

    serializer_class = VacinacaoSerializer
    permission_classes = [IsAuthenticated, IsClinicOwner]

    def get_queryset(self):
        return Vacinacao.objects.filter(
            clinica = self.request.user.clinica
        )
    
    def perform_create(self, serializer):
        print(serializer.validated_data)
        serializer.save(
            clinica=self.request.user.clinica
        )

