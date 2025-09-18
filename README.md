# Aplicação Flask em Docker

Este projeto é uma aplicação web simples construída com Flask e containerizada com Docker.

## Estrutura do Projeto

```
├── app.py                # Aplicação Flask principal
├── requirements.txt      # Dependências do Python
├── static/              # Arquivos estáticos (CSS, imagens)
├── templates/           # Templates HTML
├── Dockerfile           # Configuração do Docker
└── .dockerignore        # Arquivos a serem ignorados pelo Docker
```

## Requisitos

- Docker

## Como construir e executar o container

1. Construa a imagem Docker:

```bash
docker build -t flask-app .
```

2. Execute o container:

```bash
docker run -p 5000:5000 flask-app
```

3. Acesse a aplicação em seu navegador:

```
http://localhost:5000
```

## Desenvolvimento

Para desenvolvimento local sem Docker:

1. Crie um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute a aplicação:

```bash
python app.py
```

## Testes

Este projeto inclui testes unitários automatizados usando pytest.

### Executar os testes

```bash
# Executar todos os testes
pytest test_app.py -v

# Executar testes com cobertura
pytest test_app.py -v --cov=app --cov-report=term-missing

# Executar testes e gerar relatório HTML de cobertura
pytest test_app.py --cov=app --cov-report=html
```

### Testes incluídos

- ✅ Teste das rotas principais (/, /sobre, /nova-pagina)
- ✅ Teste de conteúdo das páginas
- ✅ Teste de rotas inexistentes (404)
- ✅ Teste de configuração da aplicação
- ✅ Teste de registro de rotas
- ✅ Teste de headers de resposta

### CI/CD

Os testes são executados automaticamente via GitHub Actions em:
- Push para a branch main
- Pull Requests para a branch main

O workflow inclui:
- Execução de testes unitários
- Relatório de cobertura de código
- Linting com flake8
- Build e teste da imagem Docker