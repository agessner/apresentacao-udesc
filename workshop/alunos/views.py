import ujson
from django import forms
from django.http import HttpResponse

from alunos.models import Aluno


def post(request):
    form = AlunoForm(request.POST)
    if form.is_valid():
        novo_aluno = Aluno(**form.cleaned_data)
        novo_aluno.save()
        return HttpResponse(status=200, content=ujson.dumps(novo_aluno))
    return HttpResponse(status=401)


class AlunoForm(forms.Form):
    nome = forms.CharField()
