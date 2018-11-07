import ujson
from django import forms
from django.http import HttpResponse

from django.views import View

from notas.models import Nota


class NotaView(View):
    def get(self, request):
        return HttpResponse(status=200)

    def post(self, request):
        form = NotaForm(request.POST)

        if form.is_valid():
            nova_nota = Nota(**form.cleaned_data)
            nova_nota.save()
            return HttpResponse(status=200, content=ujson.dumps(nova_nota))

        return HttpResponse(status=401)


class NotaForm(forms.Form):
    aluno_id = forms.IntegerField()
    valor = forms.DecimalField(decimal_places=2)
