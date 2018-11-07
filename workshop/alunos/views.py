import ujson
from django import forms
from django.http import HttpResponse

from alunos.models import Aluno
from django.shortcuts import get_object_or_404
from django.views import View


class AlunosView(View):

    def post(self, request):
        form = AlunoForm(request.POST)
        if form.is_valid():
            novo_aluno = Aluno(**form.cleaned_data)
            novo_aluno.save()
            return HttpResponse(status=200, content=ujson.dumps(novo_aluno))
        return HttpResponse(status=401)

    def get(self, request):
        alunos = Aluno.objects.all()
        return HttpResponse(status=200, content=ujson.dumps(alunos))

class AlunoView(View):

    def get(self, request, id):
        alunos = get_object_or_404(
            Aluno,
            id=id
        )
        return HttpResponse(status=200, content=ujson.dumps(alunos))


class AlunoForm(forms.Form):
    nome = forms.CharField()
