import tkinter as tk

# Lista de tarefas
tarefas = []

# Função para adicionar tarefa
def adicionar_tarefa():
    tarefa = entrada.get()
    if tarefa != "":
        tarefas.append(tarefa)
        atualizar_lista()
        entrada.delete(0, tk.END)

# Atualiza a lista na tela
def atualizar_lista():
    lista.delete(0, tk.END)
    for t in tarefas:
        lista.insert(tk.END, t)

# Janela principal
janela = tk.Tk()
janela.title("ModFlow - Gerenciador de Tarefas")

# Campo de entrada
entrada = tk.Entry(janela, width=40)
entrada.pack(pady=10)

# Botão adicionar
botao = tk.Button(janela, text="Adicionar Tarefa", command=adicionar_tarefa)
botao.pack()

# Lista de tarefas
lista = tk.Listbox(janela, width=50)
lista.pack(pady=10)

# Rodar sistema
janela.mainloop()
