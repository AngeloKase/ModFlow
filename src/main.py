import tkinter as tk

# uma lista para as tarefas
tarefas = []

# fun de adicionar a tarefa
def adicionar_tarefa():
    tarefa = entrada.get()
    if tarefa != "":
        prioridade = prioridade_var.get()
        status = status_var.get()

        tarefas.append(f"[{prioridade}] [{status}] {tarefa}")
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

# fun para editar a tarefa
def editar_tarefa():
    selecionada = lista.curselection()

    if selecionada:
        indice = selecionada[0]
        
        nova_tarefa = entrada.get()

        if nova_tarefa != "":
            prioridade = prioridade_var.get()
            status = status_var.get()

            tarefas[indice] = f"[{prioridade}] [{status}] {nova_tarefa}"
            atualizar_lista()
            entrada.delete(0, tk.END)


janela = tk.Tk()
janela.title("ModFlow - Gerenciador de Tarefas")


entrada = tk.Entry(janela, width=40)
entrada.pack(pady=10)

# prioridade da tarefa
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

# Campo de status
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

# botao do adicionar
botao = tk.Button(janela, text="Adicionar Tarefa", command=adicionar_tarefa)
botao.pack()

# botao do remover
botao_remover = tk.Button(janela, text="Remover Tarefa", command=remover_tarefa)
botao_remover.pack()

# botao para editar
botao_editar = tk.Button(janela, text="Editar Tarefa", command=editar_tarefa)
botao_editar.pack()

# lista de tarefas
lista = tk.Listbox(janela, width=50)
lista.pack(pady=10)

# janela tkinter
janela.mainloop()
