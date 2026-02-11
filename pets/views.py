from rest_framework import viewsets
from .models import Pets
from .serializers import PetsSerializer
# Create your views here.

# rotas para os pets
class PetsViewSet(viewsets.ModelViewSet):
    queryset = Pets.objects.all()
    serializer_class = PetsSerializer
