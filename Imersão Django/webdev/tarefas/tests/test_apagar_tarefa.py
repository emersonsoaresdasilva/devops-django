import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains

from webdev.tarefas.models import Tarefa

@pytest.fixture
def tarefa(db):
    return Tarefa.objects.create(nome='Tarefa 06', feita=True)

@pytest.fixture
def resposta(client, tarefa):
    resposta = client.post(
        reverse('tarefas:apagar', kwargs={'tarefa_id': tarefa.id}))
    return resposta

def test_apagar_tarefa(resposta):
    assert not Tarefa.objects.exists()