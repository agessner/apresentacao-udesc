from django.urls import path

from alunos.views import AlunoView, AlunosView, NotasView, NotaView

urlpatterns = [
    path('', AlunosView.as_view()),
    path('<int:aluno_id>', AlunoView.as_view()),
    path('<int:aluno_id>/notas', NotasView.as_view()),
    path('<int:aluno_id>/notas/<int:nota_id>', NotaView.as_view()),
]
