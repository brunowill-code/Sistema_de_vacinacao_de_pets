from rest_framework import viewsets
from .models import Vacina, Vacinacao
from .serializers import VacinacaoSerializer, VacinaSerializer
# Create your views here.

#Rotas para as Vacinas
class VacinaViewSet(viewsets.ModelViewSet):
    queryset = Vacina.objects.all()
    serializer_class = VacinaSerializer

#Rotas para as Vacinações
class VacinacaoViewSet(viewsets.ModelViewSet):
    queryset = Vacinacao.objects.all()
    serializer_class = VacinacaoSerializer


