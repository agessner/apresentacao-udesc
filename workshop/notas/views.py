import ujson
from django import forms
from django.http import HttpResponse

from django.views import View

from notas.models import Nota


class NotaListView(View):
    def get(self, request, *args, **kwargs):
        notas = Nota.objects.all()
        return HttpResponse(status=200, content=ujson.dumps(notas))

    def post(self, request):
        form = NotaForm(request.POST)

        if form.is_valid():
            nova_nota = Nota(**form.cleaned_data)
            nova_nota.save()

            todas_as_notas = Nota.objects.filter(aluno_id=nova_nota.aluno_id)
            somatorio = 0
            for nota in todas_as_notas:
                somatorio += nota.valor
            media = somatorio / len(todas_as_notas)

            nova_nota.aluno.media = media
            nova_nota.aluno.save()

            return HttpResponse(status=200, content=ujson.dumps(nova_nota))

        return HttpResponse(status=401)


class NotaView(View):

    def delete(self, request, id):
        nota_deletada = Nota.objects.get(id=id)
        nota_deletada.delete()

        todas_as_notas = Nota.objects.filter(aluno_id=nota_deletada.aluno_id)
        somatorio = 0
        for nota in todas_as_notas:
            somatorio += nota.valor
        media = somatorio / len(todas_as_notas)

        nota_deletada.aluno.media = media
        nota_deletada.aluno.save()

        return HttpResponse(status=200)


class NotaForm(forms.Form):
    aluno_id = forms.IntegerField()
    valor = forms.DecimalField(decimal_places=2)
