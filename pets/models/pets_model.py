from django.db import models

from clinic.models.clinica_model import Clinica
from clinic.models.tutor_model import Tutor


# Create your models here.
class Pets(models.Model):
    clinica = models.ForeignKey(
        Clinica,
        on_delete=models.CASCADE,
        related_name="pets"
    )
    tutor = models.ForeignKey(
        Tutor,
        on_delete=models.CASCADE,
        related_name="pets"
    )

    nome = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)   # cão, gato, etc
    raca = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10, 
                            choices=[
                                ("M", "Macho"),
                                ("F", "Fêmea"),
                            ])      # macho / fêmea
    data_de_nascimento = models.DateField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.nome
