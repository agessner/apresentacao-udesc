from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from notas.models import Nota


class NotaView(View):
    def get(self, request):
        print('shu')
        return HttpResponse(status=200)

    method_decorator(csrf_exempt)
    def post(self, request):
        print('shu2')
        nota = request.body
        Nota.save(**nota)

        return HttpResponse(status=200)
