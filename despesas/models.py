from django.db import models
from integrantes.models import Integrante

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.nome)

class FormaPagamento(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return "{}".format(self.nome) 
    
class Despesa(models.Model):
    nome = models.CharField(max_length=100)
    valorUnitario = models.DecimalField(max_digits=10, decimal_places=2)
    valorTotal = models.DecimalField(max_digits=10, decimal_places=2)
    qtdParcelas = models.IntegerField()
    data = models.DateField()
    formaPagamento = models.ForeignKey(FormaPagamento, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    integrante = models.ForeignKey(Integrante, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.nome)
    