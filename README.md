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