import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains

from webdev.tarefas.models import Tarefa

@pytest.fixture
def resposta(client, db):
    return (client.get(reverse('tarefas:home')))

def test_status_code(resposta):
    assert (resposta.status_code == 200)

def test_formulario_presente(resposta):
    assertContains(resposta, '<form')

def test_botao_salvar_presente(resposta):
    assertContains(resposta, '<button type="submit"')

@pytest.fixture
def lista_de_tarefas_pendentes(db):
    tarefas = [
        Tarefa(nome='Tarefa 01', feita=False),
        Tarefa(nome='Tarefa 02', feita=False),
        Tarefa(nome='Tarefa 03', feita=False)
    ]
    Tarefa.objects.bulk_create(tarefas)
    return tarefas

@pytest.fixture
def resposta_com_lista_de_tarefas(client, lista_de_tarefas_pendentes):
    return (client.get(reverse('tarefas:home')))

def test_lista_de_tarefas_pendentes_presentes(resposta_com_lista_de_tarefas, lista_de_tarefas_pendentes):
    for tarefa in lista_de_tarefas_pendentes:
        assertContains(resposta_com_lista_de_tarefas, tarefa.nome)
