from decimal import Decimal

import pytest
import ujson

from alunos.models import Aluno, Nota


@pytest.mark.django_db
@pytest.mark.urls('workshop.urls')
def test_atualiza_media_do_aluno_quando_adiciona_nova_nota(client):
    aluno = Aluno.objects.create(nome='marcao')
    Nota.objects.create(aluno_id=aluno.id, valor=Decimal('7.5'))

    response = client.post(f'/alunos/{aluno.id}/notas', ujson.dumps({'valor': Decimal('9.8')}), content_type='application/json')

    aluno_retornado = ujson.loads(client.get(f'/alunos/{aluno.id}').content)
    assert 200 == response.status_code
    assert 8.65 == aluno_retornado['media']


@pytest.mark.django_db
@pytest.mark.urls('workshop.urls')
def test_atualiza_media_do_aluno_quando_exclui_nota(client):
    aluno = Aluno.objects.create(nome='marcao')
    nota = Nota.objects.create(aluno_id=aluno.id, valor=Decimal('7.5'))
    Nota.objects.create(aluno_id=aluno.id, valor=Decimal('9.8'))

    response = client.delete(f'/alunos/notas/{nota.id}')

    aluno_retornado = ujson.loads(client.get(f'/alunos/{aluno.id}').content)
    assert 200 == response.status_code
    assert 9.8 == aluno_retornado['media']
