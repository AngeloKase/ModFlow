import sqlite3

# conexao com o banco de dados
conn = sqlite3.connect("data/modflow.db")
cursor = conn.cursor()

# criando a tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS tarefas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descricao TEXT,
    prioridade TEXT,
    status TEXT,
    porcentagem INTEGER
)
""")

conn.commit()


# adicionando as tarefas no banco
def adicionar_tarefa(nome, descricao, prioridade, status, porcentagem):

    cursor.execute("""
        INSERT INTO tarefas
        (nome, descricao, prioridade, status, porcentagem)

        VALUES (?, ?, ?, ?, ?)
    """, (
        nome,
        descricao,
        prioridade,
        status,
        porcentagem
    ))

    conn.commit()


# listando as tarefas do banco
def listar_tarefas():

    cursor.execute("""
        SELECT * FROM tarefas
    """)

    return cursor.fetchall()


# removendo uma tarefa do banco
def remover_tarefa(id_tarefa):

    cursor.execute("""
        DELETE FROM tarefas
        WHERE id = ?
    """, (id_tarefa,))

    conn.commit()


# editando uma tarefa do banco 
def editar_tarefa(
    id_tarefa,
    nome,
    descricao,
    prioridade,
    status,
    porcentagem
):

    cursor.execute("""
        UPDATE tarefas

        SET
            nome = ?,
            descricao = ?,
            prioridade = ?,
            status = ?,
            porcentagem = ?

        WHERE id = ?
    """, (
        nome,
        descricao,
        prioridade,
        status,
        porcentagem,
        id_tarefa
    ))

    conn.commit()