# AGATA - Agente de Gestão e Apoio Tecnológico à Agricultura

![Versão](https://img.shields.io/badge/version-1.0.0-blue.svg)

> "Conectando campos, eliminando desperdícios: Nenhum agricultor familiar sem mercado, nenhuma colheita perdida."
>

Acesso online: [family-agro-chat-agricultor](https://agata-agent-service-573130108685.us-central1.run.app/docs/)

## 📋 Sobre o Projeto

AGATA é uma solução digital que conecta agricultores familiares com prefeituras e o CONAB através de uma assistente virtual via WhatsApp. Utilizando IA generativa, a AGATA facilita o registro de produtos não vendidos nas feiras, comunica ofertas, eliminando o desperdício e aumentando a renda dos produtores rurais.

### 🌱 O Problema

Em regiões como Tangará da Serra (MT), aproximadamente 40% da produção agrícola familiar é desperdiçada por falta de canais de escoamento após as feiras. 
Ao mesmo tempo, prefeituras e o CONAB têm interesse em adquirir esses produtos, mas não possuem informações sobre disponibilidade.

### 💡 Nossa Solução

A FamilyAgro, através da AGATA, resolve este problema criando um canal direto entre produção e demanda, usando uma tecnologia já familiar aos agricultores: o WhatsApp.

## 🤖 Arquitetura de Agentes

A ÁGATA utiliza uma arquitetura multi-agente especializada:

1. **Agent Root: AGATA** - Orquestrador principal que mantém a personalidade e contexto da conversa

2. **Sub-Agents Especialistas:**
   - **StockCollector** - Extrai dados precisos sobre produtos disponíveis
   - **DealPresenter** - Comunica propostas de compra detalhadamente
   - **SaleConfirmer** - Processa aceites, ajustes ou recusas
   - **DeliveryTracker** - Gerencia logística e feedback pós-venda

## 🔄 Fluxos de Conversação

### Fluxo 1: Coleta de Dados do Produto
Captura detalhes sobre produtos disponíveis para venda, incluindo:
- Nome e variedade do produto
- Quantidade disponível
- Unidade de medida
- Prazo de validade
- Preço unitário
- Características especiais

### Fluxo 2: Comunicação de Proposta
Informa o agricultor sobre interesse de compra e apresenta detalhes:
- Comprador interessado
- Produtos solicitados com quantidades
- Preços unitários e total
- Informações logísticas

### Fluxo 3: Confirmação e Aceite
Obtém e processa a confirmação do agricultor:
- Aceites completos
- Aceites parciais com ajustes
- Recusas e motivos

### Fluxo 4: Logística e Pós-Venda
Acompanha o processo de coleta e feedback:
- Lembretes de coleta
- Verificação pós-coleta
- Avaliação de satisfação

## 💾 Modelo de Dados

O projeto utiliza MongoDB para armazenamento, com as seguintes coleções principais:

- **farmers**: Dados dos agricultores familiares
- **products**: Estoque disponível para venda
- **orders**: Pedidos e transações
- **conversations**: Histórico conversacional

## 📱 Integração e Funcionalidades MVP

- **Interface web para comunicacao por chat**: Testes para validacao em desenvolvimento
- **MongoDB**: Armazenamento em banco de dados NoSQL
- **Agent Development Kit (Google)**: Framework para desenvolvimento dos agentes de IA

## 🚀 Como Começar

### Pré-requisitos

- Python 3.9+
- MongoDB 5.0+
- API_KEY openAI

### Instalação

```bash
# Clone o repositório
[git clone https://github.com/sua-org/agata-assistant.git](https://github.com/devsergioramos/family-agro-chat-agricultor)
cd family-agro-chat-agricultor

# Instale as dependências
pip install -r requirements.txt

# Configure as variáveis de ambiente
cp .env.example .env
# Edite o arquivo .env com suas credenciais

# Inicie o servidor
make chat
```

## 📊 Métricas de Sucesso

- **Redução de desperdício**: % da produção aproveitada
- **Aumento de renda**: Incremento na renda dos agricultores
- **Adoção**: Número de agricultores usando ativamente
- **Satisfação**: NPS dos agricultores e compradores
- **Volume**: Quantidade de produtos comercializados

---

<p align="center">
  <i>Conectando os que produzem aos que precisam comprar.</i>
</p>
