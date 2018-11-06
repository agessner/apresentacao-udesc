from django.http import HttpResponse
from django.shortcuts import render

from alunos.models import Aluno


def post(request):
    aluno = request.body
    Aluno.save(**aluno)

    return HttpResponse(status=200)
