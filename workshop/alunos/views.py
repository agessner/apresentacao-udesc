import ujson
from django import forms
from django.http import HttpResponse

from alunos.models import Aluno
from django.shortcuts import get_object_or_404
from django.views import View

from alunos.models import Nota


class AlunoForm(forms.Form):
    nome = forms.CharField()


class NotaForm(forms.Form):
    valor = forms.DecimalField(decimal_places=2)


class AlunosView(View):
    def post(self, request):
        form = AlunoForm(request.POST)
        if form.is_valid():
            novo_aluno = Aluno(nome=form.cleaned_data['nome'])
            novo_aluno.save()
            return HttpResponse(status=200, content=ujson.dumps(novo_aluno), content_type='application/json')
        return HttpResponse(status=422, content_type='application/json')

    def get(self, request):
        alunos = Aluno.objects.all()
        return HttpResponse(status=200, content=ujson.dumps(alunos), content_type='application/json')


class AlunoView(View):
    def get(self, request, aluno_id):
        alunos = get_object_or_404(
            Aluno,
            id=aluno_id
        )
        return HttpResponse(status=200, content=ujson.dumps(alunos), content_type='application/json')


class NotasView(View):
    def get(self, request, aluno_id):
        notas = Nota.objects.filter(aluno_id=aluno_id)
        return HttpResponse(status=200, content=ujson.dumps(notas), content_type='application/json')

    def post(self, request, aluno_id):
        form = NotaForm(request.POST)

        if form.is_valid():
            nova_nota = Nota(aluno_id=aluno_id, valor=form.cleaned_data['valor'])
            nova_nota.save()

            todas_as_notas = Nota.objects.filter(aluno_id=nova_nota.aluno_id)
            somatorio = 0
            for nota in todas_as_notas:
                somatorio += nota.valor
            media = somatorio / len(todas_as_notas)

            nova_nota.aluno.media = media
            nova_nota.aluno.save()

            return HttpResponse(status=200, content=ujson.dumps(nova_nota), content_type='application/json')

        return HttpResponse(status=422, content_type='application/json')


class NotaView(View):
    def delete(self, request, aluno_id, nota_id):
        nota_deletada = Nota.objects.get(aluno_id=aluno_id, id=nota_id)
        nota_deletada.delete()

        todas_as_notas = Nota.objects.filter(aluno_id=nota_deletada.aluno_id)
        somatorio = 0
        for nota in todas_as_notas:
            somatorio += nota.valor
        media = somatorio / len(todas_as_notas)

        nota_deletada.aluno.media = media
        nota_deletada.aluno.save()

        return HttpResponse(status=200, content_type='application/json')
