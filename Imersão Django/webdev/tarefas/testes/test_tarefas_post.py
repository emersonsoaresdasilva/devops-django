import pytest
from django.urls import reverse
from webdev.tarefas.models import Tarefa

@pytest.fixture
def resposta(client, db):
    return (client.post(reverse('tarefas:home'), data={'nome': 'Tarefa'}))

def test_tarefa_existe_no_banco_de_dados(resposta):
    assert Tarefa.objects.exists()

def test_redirecionamento_depois_do_salvamento(resposta):
    assert (resposta.status_code == 302)

@pytest.fixture
def resposta_dado_invalido(client, db):
    return (client.post(reverse('tarefas:home'), data={'nome': ''}))

def test_tarefa_nao_existe_no_banco_de_dados(resposta_dado_invalido):
    assert not Tarefa.objects.exists()

def test_pagina_com_dados_invalidos(resposta_dado_invalido):
    assert (resposta_dado_invalido.status_code == 400)