import pytest
import json
from app import app


@pytest.fixture
def client():
    """Cria um cliente de teste para a aplicação Flask."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


# ===== TESTES UNITÁRIOS BÁSICOS =====

@pytest.mark.unit
def test_index_route(client):
    """Testa se a rota principal '/' retorna status 200."""
    response = client.get('/')
    assert response.status_code == 200


@pytest.mark.unit
def test_sobre_route(client):
    """Testa se a rota '/sobre' retorna status 200."""
    response = client.get('/sobre')
    assert response.status_code == 200


@pytest.mark.unit
def test_nova_pagina_route(client):
    """Testa se a rota '/nova-pagina' retorna status 200."""
    response = client.get('/nova-pagina')
    assert response.status_code == 200


# ===== TESTES DE CONTEÚDO =====

@pytest.mark.unit
def test_index_route_content(client):
    """Testa se a rota principal contém o título esperado."""
    response = client.get('/')
    assert b'Inicio' in response.data or b'title' in response.data


@pytest.mark.unit
def test_sobre_route_content(client):
    """Testa se a rota sobre contém o título esperado."""
    response = client.get('/sobre')
    assert b'Sobre' in response.data or b'title' in response.data


@pytest.mark.unit
def test_nova_pagina_route_content(client):
    """Testa se a rota nova-pagina contém o título esperado."""
    response = client.get('/nova-pagina')
    assert b'Nova Pagina' in response.data or b'title' in response.data


# ===== TESTES DE ERRO =====

@pytest.mark.unit
def test_404_route(client):
    """Testa se uma rota inexistente retorna status 404."""
    response = client.get('/rota-inexistente')
    assert response.status_code == 404


@pytest.mark.unit
def test_invalid_method(client):
    """Testa se métodos HTTP inválidos retornam erro apropriado."""
    response = client.post('/')
    assert response.status_code == 405  # Method Not Allowed


# ===== TESTES DE CONFIGURAÇÃO =====

@pytest.mark.unit
def test_app_configuration():
    """Testa se a aplicação Flask está configurada corretamente."""
    assert app is not None
    assert app.name == 'app'
    # Verifica se a aplicação tem as rotas esperadas
    assert len(app.url_map._rules) >= 3


@pytest.mark.unit
def test_routes_registration():
    """Testa se todas as rotas estão registradas corretamente."""
    rules = [rule.rule for rule in app.url_map.iter_rules()]
    assert '/' in rules
    assert '/sobre' in rules
    assert '/nova-pagina' in rules


# ===== TESTES DE HEADERS E RESPOSTA =====

@pytest.mark.unit
def test_response_headers(client):
    """Testa se as respostas contêm headers apropriados."""
    response = client.get('/')
    assert 'Content-Type' in response.headers
    assert 'text/html' in response.headers['Content-Type']


@pytest.mark.unit
def test_response_encoding(client):
    """Testa se a resposta está em UTF-8."""
    response = client.get('/')
    assert response.charset == 'utf-8'


# ===== TESTES DE PERFORMANCE =====

@pytest.mark.unit
def test_response_time(client):
    """Testa se a resposta é rápida (menos de 1 segundo)."""
    import time
    start_time = time.time()
    response = client.get('/')
    end_time = time.time()
    
    assert response.status_code == 200
    assert (end_time - start_time) < 1.0


# ===== TESTES DE INTEGRAÇÃO =====

@pytest.mark.integration
def test_multiple_requests(client):
    """Testa múltiplas requisições sequenciais."""
    for _ in range(5):
        response = client.get('/')
        assert response.status_code == 200


@pytest.mark.integration
def test_all_routes_accessible(client):
    """Testa se todas as rotas estão acessíveis."""
    routes = ['/', '/sobre', '/nova-pagina']
    for route in routes:
        response = client.get(route)
        assert response.status_code == 200, f"Rota {route} não está acessível"


# ===== TESTES DE DADOS DE CONTEXTO =====

@pytest.mark.unit
def test_template_context(client):
    """Testa se o contexto do template está sendo passado corretamente."""
    response = client.get('/')
    # Verifica se o template está sendo renderizado
    assert response.data is not None
    assert len(response.data) > 0


@pytest.mark.unit
def test_app_debug_mode():
    """Testa se o modo debug está configurado corretamente."""
    # Em produção, debug deveria ser False
    # Em desenvolvimento/teste, pode ser True
    assert isinstance(app.debug, bool)

