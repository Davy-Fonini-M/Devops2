# Guia de Testes - Projeto DevOps

## Visão Geral

Este projeto implementa uma cobertura de testes abrangente com testes unitários e de integração, executados automaticamente via GitHub Actions.

## Estrutura de Testes

### Testes Unitários (`@pytest.mark.unit`)
- **Testes de Rotas**: Verificação de status HTTP e conteúdo das rotas
- **Testes de Configuração**: Validação da configuração da aplicação Flask
- **Testes de Headers**: Verificação de headers HTTP apropriados
- **Testes de Performance**: Validação de tempo de resposta
- **Testes de Erro**: Verificação de tratamento de erros (404, 405)

### Testes de Integração (`@pytest.mark.integration`)
- **Múltiplas Requisições**: Teste de estabilidade com requisições sequenciais
- **Acessibilidade de Rotas**: Verificação de todas as rotas disponíveis

## Executando os Testes

### Localmente

```bash
# Instalar dependências
pip install -r requirements.txt

# Executar todos os testes
pytest

# Executar apenas testes unitários
pytest -m unit

# Executar apenas testes de integração
pytest -m integration

# Executar com cobertura
pytest --cov=app --cov-report=html --cov-report=term-missing

# Executar com cobertura mínima de 80%
pytest --cov=app --cov-fail-under=80
```

### Via GitHub Actions

Os testes são executados automaticamente:
- **Push para main/develop**: Execução completa de testes
- **Pull Requests**: Validação antes do merge
- **Agendamento**: Testes diários às 9h UTC
- **Execução Manual**: Via workflow_dispatch

## Cobertura de Testes

- **Meta de Cobertura**: 80% mínimo
- **Relatórios**: HTML e terminal
- **Upload**: Codecov para análise contínua
- **Falha**: Build falha se cobertura < 80%

## Workflows do GitHub Actions

### 1. `test.yml` - Testes Principais
- Executa em múltiplas versões do Python (3.8-3.11)
- Testes unitários e de integração
- Análise de cobertura
- Upload de relatórios
- Notificações de falha/sucesso

### 2. `alerts.yml` - Sistema de Alertas
- Notificações de PR (abertura/fechamento)
- Alertas de falha nos testes
- Notificações de deploy
- Resumos diários

### 3. `scheduled-tests.yml` - Testes Agendados
- Execução diária às 9h UTC
- Execução semanal (segunda-feira às 8h UTC)
- Verificação de qualidade do código
- Testes de performance
- Relatórios detalhados

## Configuração de Alertas

### Slack (Opcional)
Para receber notificações no Slack, configure o secret `SLACK_WEBHOOK` no GitHub:

1. Vá para Settings > Secrets and variables > Actions
2. Adicione `SLACK_WEBHOOK` com a URL do webhook do Slack

### Canais de Notificação
- `#devops-alerts`: Alertas críticos e falhas
- Notificações de PR e deploy
- Resumos de execução

## Métricas de Qualidade

### Cobertura de Código
- **app.py**: > 80% de cobertura
- **Todas as funções**: Testadas
- **Todas as rotas**: Validadas

### Performance
- **Tempo de resposta**: < 1 segundo
- **Múltiplas requisições**: Estável
- **Testes de carga**: 100 requisições em < 10 segundos

### Segurança
- **Análise estática**: Bandit
- **Vulnerabilidades**: Safety check
- **Dependências**: Verificação automática

## Troubleshooting

### Testes Falhando
1. Verificar logs do GitHub Actions
2. Executar localmente com `pytest -v`
3. Verificar cobertura com `pytest --cov=app --cov-report=term-missing`

### Cobertura Baixa
1. Adicionar testes para funções não cobertas
2. Verificar se todos os caminhos de código são testados
3. Usar `pytest --cov=app --cov-report=html` para relatório visual

### Performance Degradada
1. Verificar logs de performance nos testes agendados
2. Otimizar código se necessário
3. Ajustar thresholds se apropriado

## Contribuindo

Ao adicionar novos testes:
1. Use marcadores apropriados (`@pytest.mark.unit` ou `@pytest.mark.integration`)
2. Mantenha cobertura > 80%
3. Adicione docstrings descritivas
4. Teste cenários de sucesso e falha
5. Execute localmente antes de fazer PR

## Relatórios

- **HTML**: `htmlcov/index.html` (após execução local)
- **Codecov**: Dashboard online com histórico
- **GitHub Actions**: Logs detalhados de cada execução
- **Artifacts**: Relatórios salvos automaticamente
