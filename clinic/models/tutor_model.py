from django.db import models
from .clinica_model import Clinica

class Tutor(models.Model):
    clinica = models.ForeignKey(
        Clinica,
        on_delete=models.CASCADE,
        related_name="tutores"
    )
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=50, blank=False)
    data_de_nascimento = models.DateField()
    cpf = models.CharField(max_length=100)

    def __str__(self):
        return self.nome