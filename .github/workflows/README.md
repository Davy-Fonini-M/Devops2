# Workflows do GitHub Actions

## 🚀 Workflows Disponíveis

### 1. `simple-test.yml` - **RECOMENDADO PARA TESTE**
- ✅ **Funciona sem configurações externas**
- ✅ Executa todos os testes unitários e de integração
- ✅ Gera relatórios de cobertura
- ✅ Upload de artifacts
- ✅ Sem dependências de serviços externos

### 2. `test.yml` - Workflow Completo
- ⚠️ Requer configuração de secrets (opcional)
- ✅ Executa em múltiplas versões do Python
- ✅ Análise de segurança
- ✅ Notificações Slack (opcional)
- ✅ Upload para Codecov (opcional)

### 3. `alerts.yml` - Sistema de Alertas
- ⚠️ Requer configuração de webhook Slack
- ✅ Notificações de PR
- ✅ Alertas de falha/sucesso

### 4. `scheduled-tests.yml` - Testes Agendados
- ⚠️ Requer configuração de webhook Slack
- ✅ Execução diária
- ✅ Testes de performance

## 🔧 Configuração Recomendada

Para testar rapidamente, use apenas o `simple-test.yml`:

1. **Desabilite temporariamente** os outros workflows
2. **Use o `simple-test.yml`** que funciona sem configurações
3. **Configure os outros** apenas se necessário

## 📊 Status dos Workflows

| Workflow | Status | Dependências |
|----------|--------|--------------|
| `simple-test.yml` | ✅ Funcionando | Nenhuma |
| `test.yml` | ⚠️ Parcial | Secrets opcionais |
| `alerts.yml` | ⚠️ Parcial | Slack webhook |
| `scheduled-tests.yml` | ⚠️ Parcial | Slack webhook |

## 🎯 Para a Atividade

**Use o `simple-test.yml`** - ele executa todos os testes automaticamente em PRs sem precisar de configurações externas!
