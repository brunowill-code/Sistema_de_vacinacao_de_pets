from django.db import models
from .clinica_model import Clinica

   
class Profissional(models.Model):
    clinica = models.ForeignKey(
        Clinica,
        on_delete=models.CASCADE,
        related_name="profissionais"
    )
    nome = models.CharField(max_length=150)
    crmv = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
