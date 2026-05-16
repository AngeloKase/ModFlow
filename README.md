# 🚀 ModFlow

Sistema de gerenciamento de tarefas desenvolvido para auxiliar atividades de moderação em servidores do Discord.

O projeto foi criado utilizando conceitos de Engenharia de Software e metodologias ágeis, simulando um ambiente real de desenvolvimento com versionamento, gerenciamento de tarefas, integração contínua e controle de qualidade.

---

# 📌 Objetivo

O objetivo do ModFlow é permitir o gerenciamento eficiente de tarefas de moderação através de um sistema CRUD intuitivo e organizado.

O sistema auxilia no controle de:
- Denúncias
- Tickets
- Eventos
- Organização da equipe
- Acompanhamento de progresso de tarefas

---

# 🛠️ Tecnologias Utilizadas

- Python
- CustomTkinter
- SQLite3
- Pillow (PIL)
- GitHub Actions
- GitHub Projects
- PyTest

---

# ✨ Funcionalidades

## ✅ Tela Inicial
- Logo personalizada do servidor
- Alternância entre tema claro e escuro
- Interface moderna utilizando CustomTkinter

## ✅ Gerenciamento de Tarefas
- Criar tarefas
- Editar tarefas
- Excluir tarefas
- Visualizar tarefas

## ✅ Sistema de Organização
Cada tarefa possui:
- Título
- Descrição
- Status
- Prioridade
- Porcentagem de progresso

---

# 📂 Estrutura do Projeto

```bash
ModFlow/
│
├── docs/
├── src/
│   ├── assets/
│   ├── data/
│   └── ui/
│
├── tests/
├── main.py
├── database.py
├── README.md
└── requirements.txt
```

# 🔄 Mudança de Escopo

Inicialmente o projeto possuía apenas funcionalidades básicas de CRUD para gerenciamento de tarefas.

Durante o desenvolvimento, o escopo foi expandido para melhorar a experiência do usuário e tornar o sistema mais completo. Foram adicionadas funcionalidades como:
- Persistência de dados com SQLite3
- Sistema de prioridade
- Controle de porcentagem de progresso
- Edição individual de campos
- Tema claro e escuro
- Confirmação temporizada para exclusão de tarefas

As mudanças permitiram que o sistema se aproximasse mais de aplicações reais utilizadas em ambientes de organização e moderação.

## 🔄 Melhorias Futuras

Futuramente, o sistema será aprimorado com validações obrigatórias no cadastro de tarefas, impedindo que informações importantes sejam deixadas vazias durante a criação de uma nova tarefa.

O objetivo dessa melhoria é aumentar a confiabilidade do sistema, garantir maior integridade dos dados e melhorar a experiência do usuário durante o gerenciamento das tarefas.
