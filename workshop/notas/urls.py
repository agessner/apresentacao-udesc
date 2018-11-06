from django.urls import path

from notas.views import NotaView

urlpatterns = [
    path('', NotaView.as_view()),
]