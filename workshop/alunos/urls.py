from django.urls import path

from alunos.views import AlunoView, AlunosView, NotasView, NotaView

urlpatterns = [
    path('alunos', AlunosView.as_view()),
    path('alunos/<int:aluno_id>', AlunoView.as_view()),
    path('alunos/<int:aluno_id>/notas', NotasView.as_view()),
    path('alunos/notas/<int:nota_id>', NotaView.as_view()),
]
