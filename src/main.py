import tkinter as tk
import sqlite3


# uma lista para as tarefas
tarefas = []

# usando banco de dados
conn = sqlite3.connect("modflow.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS tarefas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tarefa TEXT,
    prioridade TEXT,
    status TEXT
)
""")

conn.commit()

# fun adicionar tarefa
def adicionar_tarefa():
    tarefa = entrada.get()
    if tarefa != "":
        prioridade = prioridade_var.get()
        status = status_var.get()

        cursor.execute(
            "INSERT INTO tarefas (tarefa, prioridade, status) VALUES (?, ?, ?)",
            (tarefa, prioridade, status)
        )

        conn.commit()

        atualizar_lista()
        entrada.delete(0, tk.END)
        atualizar_lista()
        entrada.delete(0, tk.END)

# atualizar a lista de tarefas
def atualizar_lista():
    lista.delete(0, tk.END)

    cursor.execute("SELECT tarefa, prioridade, status FROM tarefas")
    resultados = cursor.fetchall()

    for tarefa, prioridade, status in resultados:
        lista.insert(
            tk.END,
            f"[{prioridade}] [{status}] {tarefa}"
        )

# fun remover uma tarefa
def remover_tarefa():
    selecionada = lista.curselection()

    if selecionada:
        item = lista.get(selecionada)

        tarefa_texto = item.split("] ")[-1]

        cursor.execute(
            "DELETE FROM tarefas WHERE tarefa = ?",
            (tarefa_texto,)
        )

        conn.commit()

        atualizar_lista()

# fun editar uma tarefa
def editar_tarefa():
    selecionada = lista.curselection()

    if selecionada:
        item = lista.get(selecionada)

        tarefa_antiga = item.split("] ")[-1]

        nova_tarefa = entrada.get()

        prioridade = prioridade_var.get()
        status = status_var.get()

        cursor.execute("""
            UPDATE tarefas
            SET tarefa = ?, prioridade = ?, status = ?
            WHERE tarefa = ?
        """, (
            nova_tarefa,
            prioridade,
            status,
            tarefa_antiga
        ))

        conn.commit()

        atualizar_lista()

        entrada.delete(0, tk.END)


janela = tk.Tk()
janela.title("ModFlow - Gerenciador de Tarefas")


entrada = tk.Entry(janela, width=40)
entrada.pack(pady=10)

# botao de prioridade
prioridade_var = tk.StringVar()
prioridade_var.set("Média")

menu_prioridade = tk.OptionMenu(
    janela,
    prioridade_var,
    "Alta",
    "Média",
    "Baixa"
)

menu_prioridade.pack(pady=5)

# botao de status
status_var = tk.StringVar()
status_var.set("Pendente")

menu_status = tk.OptionMenu(
    janela,
    status_var,
    "Pendente",
    "Em andamento",
    "Concluída"
)

menu_status.pack(pady=5)

# botao adicionar
botao = tk.Button(janela, text="Adicionar Tarefa", command=adicionar_tarefa)
botao.pack()

# botao remover
botao_remover = tk.Button(janela, text="Remover Tarefa", command=remover_tarefa)
botao_remover.pack()

# botao editar
botao_editar = tk.Button(janela, text="Editar Tarefa", command=editar_tarefa)
botao_editar.pack()

# lista das tarefas ja adicionadas
lista = tk.Listbox(janela, width=50)
lista.pack(pady=10)

# Atualiza lista antes de iniciar
atualizar_lista()

# Rodar sistema
janela.mainloop()
