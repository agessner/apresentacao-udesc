from alunos import core
from alunos import gateways


obter_aluno = gateways.obter_aluno
obter_alunos = gateways.obter_alunos
obter_notas = gateways.obter_notas


def criar_aluno(nome):
    return core.criar_aluno(gateways.inserir_aluno, nome)


def criar_nota(aluno_id, valor):
    return core.criar_nota(gateways.obter_aluno, gateways.inserir_nota, atualizar_media_do_aluno, aluno_id, valor)


def atualizar_media_do_aluno(aluno_id):
    return core.atualizar_media_do_aluno(gateways.obter_notas, gateways.atualizar_aluno, aluno_id)


def excluir_nota(nota_id):
    return core.excluir_nota(gateways.obter_nota, gateways.excluir_nota, atualizar_media_do_aluno, nota_id)
