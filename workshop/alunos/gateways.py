from alunos.models import Nota, Aluno


def obter_aluno(aluno_id):
    return Aluno.objects.get(id=aluno_id)


def obter_alunos():
    return Aluno.objects.all()


def inserir_aluno(nome):
    return Aluno.objects.create(nome=nome)


def atualizar_aluno(aluno_id, media):
    return Aluno.objects.filter(id=aluno_id).update(media=media)


def obter_notas(aluno_id):
    return Nota.objects.filter(aluno_id=aluno_id)


def obter_nota(nota_id):
    return Nota.objects.get(id=nota_id)


def inserir_nota(aluno_id, valor):
    return Nota.objects.create(aluno_id=aluno_id, valor=valor)


def excluir_nota(nota_id):
    return Nota.objects.get(id=nota_id).delete()
