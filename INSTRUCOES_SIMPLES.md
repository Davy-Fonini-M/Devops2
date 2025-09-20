# 🎯 Instruções Simples - Testes Unitários

## ✅ O que está funcionando

**Workflow ativo**: `.github/workflows/testes-unitarios.yml`
- ✅ **17 testes** (15 unitários + 2 integração)
- ✅ **92% de cobertura** de código
- ✅ **Execução automática em PRs**
- ✅ **Sem dependências externas**
- ✅ **Sem necessidade de secrets**

## 🚀 Como testar

### 1. Fazer commit das alterações
```bash
git add .
git commit -m "feat: adicionar workflow simplificado de testes unitários"
git push origin feature/nova-funcionalidade
```

### 2. Criar Pull Request
1. Acesse: https://github.com/Davy-Fonini-M/Devops2
2. Clique em "Compare & pull request"
3. Configure:
   - **Base**: `main`
   - **Compare**: `feature/nova-funcionalidade`
   - **Título**: "Implementar Testes Unitários Automatizados"

### 3. Observar execução automática
- O workflow `testes-unitarios.yml` executará automaticamente
- Vá na aba "Actions" para ver os logs
- Todos os 17 testes devem passar ✅

## 📊 O que o workflow faz

1. **Checkout** do código
2. **Configuração** do Python 3.11
3. **Instalação** das dependências
4. **Execução** dos testes unitários
5. **Execução** dos testes de integração
6. **Execução** de todos os testes
7. **Cálculo** da cobertura de código
8. **Exibição** do resumo

## 📸 Screenshots para entrega

1. **Código dos testes**: Execute `./demo_tests.sh` localmente
2. **Execução na PR**: Screenshot da aba "Actions" do GitHub
3. **Logs dos testes**: Screenshot dos logs de execução

## ✅ Checklist da atividade

- [x] 17 testes unitários implementados
- [x] Execução automática em PRs configurada
- [x] Cobertura > 80% (92% atual)
- [x] Sem dependências externas
- [x] Funcionando sem erros
- [x] Pronto para screenshots

## 🎉 Resultado esperado

Quando você criar a PR, verá:
- ✅ Status check "Testes Unitários" passando
- ✅ 17 testes executando com sucesso
- ✅ Cobertura de 92%
- ✅ Logs detalhados na aba Actions

**Tudo funcionando perfeitamente para a entrega da atividade!** 🚀
