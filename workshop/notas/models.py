from django.db import models

from alunos.models import Aluno


class Nota(models.Model):
    valor = models.DecimalField(decimal_places=2, max_digits=9)
    aluno = models.ForeignKey(Aluno, on_delete=False)

    @property
    def nota_id(self):
        return self.id
