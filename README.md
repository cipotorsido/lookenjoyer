
# 👗 Fabio – Assistente de Moda Inteligente

![Versão](https://img.shields.io/badge/version-1.0.0-blue.svg)

> “O look certo para a ocasião certa: estilo, conforto e confiança com a ajuda da IA.”

📄 Acesso à documentação: _em breve_

---

## 📋 Sobre o Projeto

**Fabio** é um sistema conversacional com IA generativa, desenvolvido para ajudar pessoas a escolherem roupas apropriadas para diferentes ocasiões.  
A interação ocorre de forma natural via **WhatsApp**, utilizando uma linguagem amigável, leve e personalizada.

A solução foca em combinar o estilo pessoal do usuário com o contexto do evento, levando em conta dados como local, tipo de ambiente, estilo musical e preferências individuais.

---

### 🎯 O Problema

Muitas pessoas têm dificuldade em escolher o que vestir para determinados eventos, como festas, shows, encontros ou ambientes profissionais. Isso gera insegurança, atrasos e até desconforto.

Ao mesmo tempo, as soluções atuais de moda são genéricas, sem considerar o contexto real ou o estilo de quem está pedindo ajuda.

---

### 💡 Nossa Solução

A **Fabio** resolve isso oferecendo sugestões personalizadas de looks, com base em:
- Dados do usuário (idade, corpo, estilo pessoal)
- Contexto do evento (local, música, ambiente, horário, clima)

Tudo isso via uma plataforma acessível e familiar: o **WhatsApp**.

---

## 🧠 Arquitetura de Agentes

Fabio utiliza uma arquitetura multiagente com orquestração via **Google Agent Development Kit (ADK)**.

### 1. Agente Raiz: `Fabio`
Orquestrador principal que conduz o diálogo com o usuário e aciona agentes especialistas conforme o fluxo da conversa.

### 2. Subagentes Especialistas
- **UserProfileAgent** – Coleta informações do perfil pessoal do usuário  
- **EventContextAgent** – Recolhe dados do evento ou ocasião  
- **LookRecommenderAgent** – Gera sugestões personalizadas de roupas  
- **FeedbackAgent** – Coleta feedback para melhoria contínua

---

## 🔄 Fluxos de Conversação

### Fluxo 1: Coleta de Perfil do Usuário
- Nome e idade
- Sexo/gênero
- Tipo corporal
- Estilo pessoal (casual, ousado, confortável, etc.)

### Fluxo 2: Entendimento do Evento
- Tipo de evento (festa, churrasco, casamento, entrevista)
- Local e ambiente (grama, terra, piso, salão)
- Estilo musical predominante
- Clima e horário

### Fluxo 3: Recomendação de Look
Gera uma sugestão personalizada com:
- Combinação de peças
- Justificativa da escolha
- Alternativas, se desejado

### Fluxo 4: Feedback e Ajustes
- Reações, ajustes ou novos pedidos
- Registro de preferências futuras

---

## 💾 Modelo de Dados

Estrutura recomendada (MongoDB, PostgreSQL ou Firebase):

- **users**: Perfil do usuário
- **events**: Contexto da ocasião
- **looks**: Sugestões geradas e feedbacks
- **conversations**: Histórico da interação

---

## 📱 Integração e Funcionalidades MVP

- Integração com **WhatsApp API (Meta)** ou **Twilio**
- Orquestração com **Google Agent Development Kit (ADK)**
- IA generativa com **OpenAI GPT-4** (ou similar)
- Banco de dados estruturado para perfis/contextos

---

## 🚀 Como Começar

### Pré-requisitos

- Python 3.10+
- MongoDB ou Firebase
- Conta no WhatsApp Business (Meta) ou Twilio
- API Key OpenAI

### Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/Fabio-assistant.git
cd Fabio-assistant

# Instale as dependências
pip install -r requirements.txt

# Configure as variáveis de ambiente
cp .env.example .env
# Edite o .env com suas chaves do OpenAI e credenciais do WhatsApp

# Rode o servidor de chat
make chat
```

---

## 📊 Métricas de Sucesso

- **Satisfação**: Avaliações positivas dos looks sugeridos  
- **Retenção**: Quantos usuários retornam  
- **Tempo de resposta**: Agilidade no atendimento  
- **Diversidade**: Ocasiões e estilos atendidos  
- **Feedbacks**: Comentários úteis para melhoria

---

<p align="center">
  <i>"Ajudando você a se vestir bem para viver melhor."</i>
</p>
