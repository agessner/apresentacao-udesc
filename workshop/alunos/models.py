from django.db import models


class Aluno(models.Model):
    nome = models.TextField()
    media = models.DecimalField(decimal_places=2, max_digits=9, null=True, blank=True)


class Nota(models.Model):
    valor = models.DecimalField(decimal_places=2, max_digits=9)
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
