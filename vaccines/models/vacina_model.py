from django.db import models
from clinic.models.clinica_model import Clinica
from clinic.models.profissional_model import Profissional
from pets.models.pets_model import Pets

class Vacina(models.Model):
    clinica = models.ForeignKey(
        Clinica,
        on_delete=models.CASCADE,
        related_name="vacinas"
    )

    nome = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100)
    lote = models.CharField(max_length=50)

    data_fabricacao = models.DateField()
    data_validade = models.DateField()

    descricao = models.CharField(max_length=200)

    ESPECIE_CHOICES = [
        ("CANINA", "Canina"),
        ("FELINA", "Felina"),
    ]

    especie_indicada = models.CharField(
        max_length=10,
        choices=ESPECIE_CHOICES
    )

    intervalo_doses_dias = models.IntegerField()
    quantidade_estoque = models.IntegerField()

    def __str__(self):
        return f"{self.nome} - Lote {self.lote}"