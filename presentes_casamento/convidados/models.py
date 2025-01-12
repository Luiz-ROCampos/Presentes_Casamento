from django.db import models
from noivos.models import Convidados
# Create your models here.

class Acompanhantes(models.Model):
    nome_acompanhante = models.CharField(max_length=100)
    acompanhante_de = models.ForeignKey(Convidados, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.nome_acompanhante