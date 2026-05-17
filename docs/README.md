# 📊 Diagramas do Projeto

Esta seção apresenta os principais diagramas utilizados durante o desenvolvimento do ModFlow, auxiliando na modelagem, organização e documentação do sistema.

Os diagramas foram criados seguindo conceitos de Engenharia de Software para representar tanto a estrutura interna do sistema quanto suas funcionalidades principais.

---

# 🧩 Diagrama de Classes

O Diagrama de Classes representa a estrutura do sistema, mostrando as classes principais, seus atributos, métodos e relacionamentos.

No ModFlow, o diagrama demonstra:
- Estrutura das tarefas
- Integração com o banco de dados SQLite3
- Organização das interfaces do sistema
- Comunicação entre telas e funcionalidades

## 📌 Principais Elementos

### ✅ Classe Tarefas
Responsável pelo armazenamento das informações das tarefas:
- ID
- Nome
- Descrição
- Prioridade
- Status
- Porcentagem de progresso

Também contém os métodos principais do CRUD:
- adicionar()
- editar()
- remover()
- listar()

---

### ✅ Classe Banco de Dados
Responsável pela persistência das informações utilizando SQLite3.

Realiza:
- Inserção de tarefas
- Atualização de dados
- Remoção de registros
- Consulta de tarefas

---

### ✅ Interfaces UI
As interfaces representam as telas do sistema:
- Menu UI
- Ver Tarefas UI
- Editar Tarefa UI

Essas telas realizam a interação direta com o usuário.

---

## 🖼️ Diagrama de Classes

<p align="center">
  <img src="docs/diagrama-classes.png" width="850">
</p>

---

# 🎯 Diagrama de Casos de Uso

O Diagrama de Casos de Uso representa as funcionalidades disponíveis para o usuário dentro do sistema.

Ele demonstra como o usuário interage com o ModFlow e quais ações podem ser realizadas.

---

## 📌 Funcionalidades Representadas

### ✅ Gerenciamento de Tarefas
O usuário pode:
- Criar tarefas
- Editar tarefas
- Excluir tarefas
- Visualizar tarefas

---

### ✅ Organização do Fluxo
O sistema também permite:
- Definir prioridade
- Gerenciar progresso
- Alterar tema da interface

---

## 👤 Ator Principal

O ator principal do sistema é o usuário/moderador, responsável pelo gerenciamento das tarefas dentro da aplicação.

---

## 🖼️ Diagrama de Casos de Uso

<p align="center">
  <img src="docs/diagrama-casos-uso.png" width="850">
</p>

---

# 📚 Importância dos Diagramas

Os diagramas foram fundamentais para:
- Planejamento da arquitetura
- Organização das funcionalidades
- Estruturação do banco de dados
- Visualização das relações do sistema
- Facilidade de manutenção e evolução do projeto

Além disso, auxiliaram no entendimento geral do sistema durante o desenvolvimento e documentação do projeto.
