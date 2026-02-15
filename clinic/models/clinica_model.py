from django.db import models
from setup import settings

class Clinica(models.Model):
    nome = models.CharField(max_length=100)
    owner = models.OneToOneField(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
            related_name="clinica"
        )

    def __str__ (self):
        return self.nome