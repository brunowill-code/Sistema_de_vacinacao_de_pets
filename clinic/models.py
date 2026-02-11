from django.db import models

class Clinica(models.Model):
    nome = models.CharField(max_length=100)
    def __str__ (self):
        return self.nome

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
