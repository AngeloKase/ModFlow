import tkinter as tk

# uma lista para as tarefas
tarefas = []

# fun de adicionar a tarefa
def adicionar_tarefa():
    tarefa = entrada.get()
    if tarefa != "":
        tarefas.append(tarefa)
        atualizar_lista()
        entrada.delete(0, tk.END)

# fun para a lista ficar atualizada
def atualizar_lista():
    lista.delete(0, tk.END)
    for t in tarefas:
        lista.insert(tk.END, t)

# fun para remover a tarefa selecionada
def remover_tarefa():
    selecionada = lista.curselection()

    if selecionada:
        indice = selecionada[0]
        tarefas.pop(indice)
        atualizar_lista()


janela = tk.Tk()
janela.title("ModFlow - Gerenciador de Tarefas")


entrada = tk.Entry(janela, width=40)
entrada.pack(pady=10)

# botao do adicionar
botao = tk.Button(janela, text="Adicionar Tarefa", command=adicionar_tarefa)
botao.pack()

# botao do remover
botao_remover = tk.Button(janela, text="Remover Tarefa", command=remover_tarefa)
botao_remover.pack()

# lista de tarefas
lista = tk.Listbox(janela, width=50)
lista.pack(pady=10)

# janela tkinter
janela.mainloop()
