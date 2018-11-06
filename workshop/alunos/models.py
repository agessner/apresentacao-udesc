from django.db import models


class Aluno(models.Model):
    nome = models.TextField()
    media = models.DecimalField(decimal_places=2, max_digits=9)
