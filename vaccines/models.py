from django.db import models
from clinic.models import Clinica, Profissional
from pets.models import Pets

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
    
class Vacinacao(models.Model):
    clinica = models.ForeignKey(
        Clinica,
        on_delete=models.CASCADE,
        related_name="vacinacoes"
    )

    pet = models.ForeignKey(
        Pets,
        on_delete=models.CASCADE,
        related_name="vacinacoes"
    )

    vacina = models.ForeignKey(
        Vacina,
        on_delete=models.CASCADE,
        related_name="aplicacoes"
    )

    profissional = models.ForeignKey(
        Profissional,
        on_delete=models.CASCADE,
        null=False,
        related_name="vacinacoes"
    )

    data_aplicacao = models.DateField(auto_now_add=True, blank=False)
    proxima_dose = models.DateField()
    observacoes = models.CharField(max_length=200, blank=True)

    def __str__(self):
            return f"{self.pet} - {self.vacina}"