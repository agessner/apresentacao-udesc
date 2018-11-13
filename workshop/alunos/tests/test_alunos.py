import json as ujson

import pytest

from alunos.services import criar_aluno, criar_nota, obter_aluno


@pytest.mark.django_db
@pytest.mark.urls('workshop.urls')
def test_cria_aluno(client):
    response = client.post(f'/alunos', ujson.dumps({'nome': 'Marcão'}), content_type='application/json')

    assert 200 == response.status_code


@pytest.mark.django_db
@pytest.mark.urls('workshop.urls')
def test_obtem_aluno_por_id(client):
    nome = 'Marcão'
    aluno_esperado = criar_aluno(nome)

    response = client.get(f'/alunos/{aluno_esperado.id}')

    aluno_retornado = ujson.loads(response.content)
    assert 200 == response.status_code
    assert nome == aluno_retornado['nome']


@pytest.mark.django_db
@pytest.mark.urls('workshop.urls')
def test_obtem_notas_de_um_aluno(client):
    aluno = criar_aluno('Marcão')
    criar_nota(aluno.id, 7.0)
    criar_nota(aluno.id, 8.0)

    response = client.get(f'/alunos/{aluno.id}/notas')

    notas = ujson.loads(response.content)
    assert 200 == response.status_code
    assert 2 == len(notas)


@pytest.mark.django_db
@pytest.mark.urls('workshop.urls')
def test_gravar_nota_de_um_aluno(client):
    valor = 8.0
    aluno = criar_aluno('Marcão')

    response = client.post(f'/alunos/{aluno.id}/notas', ujson.dumps({'valor': valor}), content_type='application/json')

    nota = ujson.loads(response.content)
    assert 200 == response.status_code
    assert valor == nota['valor']


@pytest.mark.django_db
@pytest.mark.urls('workshop.urls')
def test_exclui_nota_de_um_aluno(client):
    aluno = criar_aluno('Marcão')
    nota = criar_nota(aluno.id, 8.0)

    response = client.delete(f'/alunos/notas/{nota.id}')

    assert 200 == response.status_code


@pytest.mark.django_db
@pytest.mark.urls('workshop.urls')
def test_obtem_todos_os_alunos(client):
    criar_aluno('Marcão')
    criar_aluno('João')

    response = client.get('/alunos')

    aluno_retornado = ujson.loads(response.content)
    assert 200 == response.status_code
    assert 2 == len(aluno_retornado)


@pytest.mark.django_db
@pytest.mark.urls('workshop.urls')
def test_atualiza_media_do_aluno_quando_adiciona_nova_nota(client):
    aluno = criar_aluno('Marcão')
    criar_nota(aluno.id, 7.5)

    response = client.post(f'/alunos/{aluno.id}/notas', ujson.dumps({'valor': 9.8}), content_type='application/json')

    aluno_retornado = obter_aluno(aluno.id)
    assert 200 == response.status_code
    assert 8.65 == aluno_retornado.media


@pytest.mark.django_db
@pytest.mark.urls('workshop.urls')
def test_atualiza_media_do_aluno_quando_exclui_nota(client):
    aluno = criar_aluno('Marcão')
    nota = criar_nota(aluno.id, 7.5)
    criar_nota(aluno.id, 9.8)

    response = client.delete(f'/alunos/notas/{nota.id}')

    aluno_retornado = obter_aluno(aluno.id)
    assert 200 == response.status_code
    assert 9.8 == aluno_retornado.media
