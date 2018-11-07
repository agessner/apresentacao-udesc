from django.urls import path

from alunos.views import AlunoView, AlunosView


urlpatterns = [
    path('', AlunosView.as_view()),
    path('<int:id>/', AlunoView.as_view()),
]