import ujson

from django import forms
from django.http import HttpResponse
from django.views import View

from alunos.services import criar_aluno, obter_aluno, obter_alunos, obter_notas, criar_nota, excluir_nota


class AlunoForm(forms.Form):
    nome = forms.CharField()


class NotaForm(forms.Form):
    valor = forms.DecimalField(decimal_places=2)


class AlunosView(View):
    def post(self, request):
        body = ujson.loads(request.body)
        novo_aluno = criar_aluno(body['nome'])
        return HttpResponse(status=200, content=ujson.dumps(novo_aluno), content_type='application/json')

    def get(self, request):
        alunos = obter_alunos()
        return HttpResponse(status=200, content=ujson.dumps(alunos), content_type='application/json')


class AlunoView(View):
    def get(self, request, aluno_id):
        aluno = obter_aluno(aluno_id)
        return HttpResponse(status=200, content=ujson.dumps(aluno), content_type='application/json')


class NotasView(View):
    def get(self, request, aluno_id):
        notas = obter_notas(aluno_id)
        return HttpResponse(status=200, content=ujson.dumps(notas), content_type='application/json')

    def post(self, request, aluno_id):
        body = ujson.loads(request.body)
        nota = criar_nota(aluno_id, body['valor'])
        return HttpResponse(status=200, content=ujson.dumps(nota), content_type='application/json')


class NotaView(View):
    def delete(self, request, nota_id):
        excluir_nota(nota_id)
        return HttpResponse(status=200, content_type='application/json')
