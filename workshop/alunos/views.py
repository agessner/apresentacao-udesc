import json as ujson

from django.http import HttpResponse
from django.views import View

from alunos.services import criar_aluno, obter_aluno, obter_alunos, obter_notas, criar_nota, excluir_nota


class AlunosView(View):
    def post(self, request):
        body = ujson.loads(request.body)
        aluno = criar_aluno(body['nome'])
        return HttpResponse(status=200, content=ujson.dumps(apresentar_aluno(aluno)), content_type='application/json')

    def get(self, request):
        alunos = obter_alunos()
        return HttpResponse(status=200, content=ujson.dumps(apresentar_alunos(alunos)), content_type='application/json')


class AlunoView(View):
    def get(self, request, aluno_id):
        aluno = obter_aluno(aluno_id)
        return HttpResponse(status=200, content=ujson.dumps(apresentar_aluno(aluno)), content_type='application/json')


class NotasView(View):
    def get(self, request, aluno_id):
        notas = obter_notas(aluno_id)
        return HttpResponse(status=200, content=ujson.dumps(apresentar_notas(notas)), content_type='application/json')

    def post(self, request, aluno_id):
        body = ujson.loads(request.body)
        nota = criar_nota(aluno_id, body['valor'])
        return HttpResponse(status=200, content=ujson.dumps(apresentar_nota(nota)), content_type='application/json')


class NotaView(View):
    def delete(self, request, nota_id):
        excluir_nota(nota_id)
        return HttpResponse(status=200, content_type='application/json')


def apresentar_aluno(aluno):
    return {
        'id': aluno.id,
        'media': aluno.media,
        'nome': aluno.nome,
    }


def apresentar_alunos(alunos):
    return [apresentar_aluno(aluno) for aluno in alunos]


def apresentar_nota(nota):
    return {
        'id': nota.id,
        'aluno_id': nota.aluno_id,
        'valor': nota.valor
    }


def apresentar_notas(notas):
    return [apresentar_nota(nota) for nota in notas]
