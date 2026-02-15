from rest_framework import viewsets ,mixins
from ..models.vacinacao_model import  Vacinacao
from ..serializers.vacinacao_serializer import VacinacaoSerializer
from setup.permissions import IsClinicOwner
from rest_framework.permissions import IsAuthenticated

#Rotas para as Vacinações
class VacinacaoViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = VacinacaoSerializer
    permission_classes = [IsAuthenticated, IsClinicOwner]

    def get_queryset(self):
        return Vacinacao.objects.filter(
            clinica=self.request.user.clinica
        )

    def perform_create(self, serializer):
        serializer.save(
            clinica=self.request.user.clinica
        )

