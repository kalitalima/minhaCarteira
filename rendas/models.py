from django.db import models
from integrantes.models import Integrante

# Create your models here.
class Renda(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()
    integrante = models.ForeignKey(Integrante, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.nome)