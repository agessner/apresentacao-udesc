from django.urls import path

from notas.views import NotaView, NotaListView


urlpatterns = [
    path('', NotaListView.as_view()),
    path('<int:id>/', NotaView.as_view()),
]