import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains

@pytest.fixture
def resposta(client):
    return client.get(reverse('tarefas:home'))

def test_status_code(resposta):
    assert (resposta.status_code == 200)

def test_formulario_presente(resposta):
    assertContains(resposta, '<form')

def test_botao_salvar_presente(resposta):
    assertContains(resposta, '<button type="submit"')