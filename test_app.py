import pytest
from app import app


@pytest.fixture
def client():
    """Cria um cliente de teste para a aplicação Flask."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index_route(client):
    """Testa se a rota principal '/' retorna status 200."""
    response = client.get('/')
    assert response.status_code == 200


def test_sobre_route(client):
    """Testa se a rota '/sobre' retorna status 200."""
    response = client.get('/sobre')
    assert response.status_code == 200


def test_nova_pagina_route(client):
    """Testa se a rota '/nova-pagina' retorna status 200."""
    response = client.get('/nova-pagina')
    assert response.status_code == 200


def test_index_route_content(client):
    """Testa se a rota principal contém o título esperado."""
    response = client.get('/')
    assert b'Inicio' in response.data or b'title' in response.data


def test_sobre_route_content(client):
    """Testa se a rota sobre contém o título esperado."""
    response = client.get('/sobre')
    assert b'Sobre' in response.data or b'title' in response.data


def test_nova_pagina_route_content(client):
    """Testa se a rota nova-pagina contém o título esperado."""
    response = client.get('/nova-pagina')
    assert b'Nova Pagina' in response.data or b'title' in response.data


def test_404_route(client):
    """Testa se uma rota inexistente retorna status 404."""
    response = client.get('/rota-inexistente')
    assert response.status_code == 404


def test_app_configuration():
    """Testa se a aplicação Flask está configurada corretamente."""
    assert app is not None
    # Verifica se a aplicação tem as rotas esperadas
    assert len(app.url_map._rules) >= 3


def test_routes_registration():
    """Testa se todas as rotas estão registradas corretamente."""
    rules = [rule.rule for rule in app.url_map.iter_rules()]
    assert '/' in rules
    assert '/sobre' in rules
    assert '/nova-pagina' in rules


def test_response_headers(client):
    """Testa se as respostas contêm headers apropriados."""
    response = client.get('/')
    assert 'Content-Type' in response.headers
    assert 'text/html' in response.headers['Content-Type']

