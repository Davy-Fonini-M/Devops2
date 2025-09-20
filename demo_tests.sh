#!/bin/bash

# Script de Demonstração - Testes Unitários e GitHub Actions
# Projeto DevOps - Semana 7

echo "🚀 DEMONSTRAÇÃO DO SISTEMA DE TESTES"
echo "====================================="
echo ""

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Função para imprimir com cores
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Verificar se Python está instalado
print_status "Verificando instalação do Python..."
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
    print_success "Python3 encontrado"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
    print_success "Python encontrado"
else
    print_error "Python não encontrado. Instale Python 3.8+ para continuar."
    exit 1
fi

# Verificar versão do Python
PYTHON_VERSION=$($PYTHON_CMD --version 2>&1 | cut -d' ' -f2 | cut -d'.' -f1,2)
print_status "Versão do Python: $PYTHON_VERSION"

# Instalar dependências
print_status "Instalando dependências..."
$PYTHON_CMD -m pip install --upgrade pip -q
$PYTHON_CMD -m pip install -r requirements.txt -q

if [ $? -eq 0 ]; then
    print_success "Dependências instaladas com sucesso"
else
    print_error "Falha ao instalar dependências"
    exit 1
fi

echo ""
echo "📊 EXECUTANDO TESTES UNITÁRIOS"
echo "==============================="

# Executar testes unitários
print_status "Executando testes unitários..."
$PYTHON_CMD -m pytest -m unit -v --tb=short

if [ $? -eq 0 ]; then
    print_success "Todos os testes unitários passaram!"
else
    print_error "Alguns testes unitários falharam"
fi

echo ""
echo "🔗 EXECUTANDO TESTES DE INTEGRAÇÃO"
echo "=================================="

# Executar testes de integração
print_status "Executando testes de integração..."
$PYTHON_CMD -m pytest -m integration -v --tb=short

if [ $? -eq 0 ]; then
    print_success "Todos os testes de integração passaram!"
else
    print_error "Alguns testes de integração falharam"
fi

echo ""
echo "📈 RELATÓRIO DE COBERTURA"
echo "========================="

# Executar com cobertura
print_status "Gerando relatório de cobertura..."
$PYTHON_CMD -m pytest --cov=app --cov-report=term-missing --cov-report=html

if [ $? -eq 0 ]; then
    print_success "Relatório de cobertura gerado com sucesso!"
    print_status "Relatório HTML disponível em: htmlcov/index.html"
else
    print_error "Falha ao gerar relatório de cobertura"
fi

echo ""
echo "🧪 EXECUTANDO TODOS OS TESTES"
echo "============================="

# Executar todos os testes
print_status "Executando bateria completa de testes..."
$PYTHON_CMD -m pytest -v --tb=short

if [ $? -eq 0 ]; then
    print_success "🎉 TODOS OS TESTES PASSARAM!"
else
    print_error "❌ Alguns testes falharam"
fi

echo ""
echo "📋 RESUMO DOS TESTES"
echo "===================="

# Contar testes
TOTAL_TESTS=$($PYTHON_CMD -m pytest --collect-only -q | grep -c "test session starts" -A 1000 | grep -c "test_" || echo "0")
UNIT_TESTS=$($PYTHON_CMD -m pytest -m unit --collect-only -q | grep -c "test_" || echo "0")
INTEGRATION_TESTS=$($PYTHON_CMD -m pytest -m integration --collect-only -q | grep -c "test_" || echo "0")

echo "Total de testes: $TOTAL_TESTS"
echo "Testes unitários: $UNIT_TESTS"
echo "Testes de integração: $INTEGRATION_TESTS"

echo ""
echo "🚀 GITHUB ACTIONS"
echo "================="
echo "Os workflows do GitHub Actions estão configurados para:"
echo "• Executar testes automaticamente em PRs"
echo "• Executar testes em push para main/develop"
echo "• Executar testes agendados diariamente"
echo "• Enviar notificações de falha/sucesso"
echo "• Gerar relatórios de cobertura"
echo "• Fazer upload para Codecov"

echo ""
echo "📁 ARQUIVOS CRIADOS"
echo "==================="
echo "• .github/workflows/test.yml - Workflow principal de testes"
echo "• .github/workflows/alerts.yml - Sistema de alertas"
echo "• .github/workflows/scheduled-tests.yml - Testes agendados"
echo "• codecov.yml - Configuração do Codecov"
echo "• TESTING.md - Documentação dos testes"
echo "• pytest.ini - Configuração do pytest"

echo ""
echo "✅ DEMONSTRAÇÃO CONCLUÍDA!"
echo "=========================="
echo "Para testar o GitHub Actions:"
echo "1. Faça commit das alterações"
echo "2. Crie uma Pull Request"
echo "3. Observe os testes executando automaticamente"
echo "4. Verifique as notificações (se configurado Slack)"

echo ""
print_success "Sistema de testes implementado com sucesso! 🎉"
