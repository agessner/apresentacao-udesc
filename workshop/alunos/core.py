from decimal import Decimal


def criar_aluno(inserir_aluno_no_bd, nome):
    validar_aluno(nome)
    return inserir_aluno_no_bd(nome)


def criar_nota(obter_aluno_do_bd, inserir_nota_no_bd, atualizar_media_do_aluno, aluno_id, valor):
    aluno = obter_aluno_do_bd(aluno_id)
    validar_nota(valor)
    nota = inserir_nota_no_bd(aluno.id, valor)
    atualizar_media_do_aluno(aluno.id)
    return nota


def excluir_nota(obter_nota_do_bd, excluir_nota_no_bd, atualizar_media_do_aluno, nota_id):
    nota = obter_nota_do_bd(nota_id)
    excluir_nota_no_bd(nota.id)
    atualizar_media_do_aluno(nota.aluno_id)


def atualizar_media_do_aluno(obter_notas_do_bd, atualizar_aluno_no_bd, aluno_id):
    todas_as_notas = obter_notas_do_bd(aluno_id)

    quantidade_de_notas = len(todas_as_notas)
    if quantidade_de_notas == 0:
        return atualizar_aluno_no_bd(aluno_id, media=None)

    somatorio = 0
    for nota in todas_as_notas:
        somatorio += nota.valor
    media = somatorio / len(todas_as_notas)

    return atualizar_aluno_no_bd(aluno_id, media)


def validar_aluno(nome):
    if not isinstance(nome, str):
        raise TypeError()

    if not nome:
        raise ValueError('Nome deve ser informado')


def validar_nota(nota):
    nota = Decimal(str(nota))

    if nota < 0:
        raise ValueError('Nota deve ser maior ou igual a zero')

    if nota > 10:
        raise ValueError('Nota deve ser menor ou igual a dez')
