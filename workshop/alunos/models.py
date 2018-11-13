from django.db import models


class Aluno(models.Model):
    nome = models.TextField()
    media = models.FloatField(null=True, blank=True)


class Nota(models.Model):
    valor = models.FloatField()
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
