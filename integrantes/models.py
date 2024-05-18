from django.db import models

# Create your models here.
class Integrante(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return "{}".format(self.nome)
