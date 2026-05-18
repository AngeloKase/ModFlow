import customtkinter as ctk
import textwrap

from database import (
    listar_tarefas,
    editar_tarefa
)

# Cores

TEXT_COLOR = ("#111111", "#ffffff")
SECOND_TEXT = ("#555555", "#aaaaaa")

PURPLE = "#c77dff"
PURPLE_HOVER = "#a855f7"
GREEN = "#4ade80"

# Fun para voltar para o menu

def voltar_menu(app):

    from ui.menu import abrir_menu

    abrir_menu(app)


def tela_sucesso_edicao(app, nome):

    for widget in app.winfo_children():
        widget.destroy()

    sucesso_frame = ctk.CTkFrame(
        app,
        fg_color="transparent"
    )

    sucesso_frame.pack(expand=True)

    titulo_sucesso = ctk.CTkLabel(
        sucesso_frame,
        text="Tarefa editada com sucesso!",
        font=("Segoe UI", 34, "bold"),
        text_color=GREEN
    )

    titulo_sucesso.pack(
        pady=(20, 15)
    )

    subtitulo = ctk.CTkLabel(
        sucesso_frame,
        text=f'"{nome}" foi atualizada no sistema.',
        font=("Segoe UI", 18),
        text_color=TEXT_COLOR
    )

    subtitulo.pack(
        pady=(0, 30)
    )

    voltar_menu_btn = ctk.CTkButton(
        sucesso_frame,
        text="Voltar ao Menu",
        width=250,
        height=55,
        fg_color=PURPLE,
        hover_color=PURPLE_HOVER,
        font=("Segoe UI", 17, "bold"),
        command=lambda: voltar_menu(app)
    )

    voltar_menu_btn.pack()


# Fun abrir tela de editar tarefa

def abrir_editar_task(app):

    # limpar tela
    for widget in app.winfo_children():
        widget.destroy()

    # frame principal
    frame = ctk.CTkScrollableFrame(
        app,
        fg_color="transparent"
    )

    frame.pack(
        expand=True,
        fill="both",
        padx=20,
        pady=20
    )

    # voltar
    voltar_btn = ctk.CTkButton(
        frame,
        text="← Voltar",
        width=120,
        height=40,
        fg_color= PURPLE,
        hover_color= PURPLE_HOVER,
        command=lambda: voltar_menu(app)
    )

    voltar_btn.pack(
        anchor="w",
        pady=(0, 20)
    )

    # titulo
    titulo = ctk.CTkLabel(
        frame,
        text="Editar Tarefas",
        font=("Segoe UI", 32, "bold")
    )

    titulo.pack(pady=(0, 30))
    
    tarefas = listar_tarefas()
    

    # listar tarefas
    for tarefa in tarefas:

        tarefa_frame = ctk.CTkFrame(
            frame,
            corner_radius=15
        )

        tarefa_frame.pack(
            fill="x",
            pady=10,
            padx=10
        )

        descricao_formatada = textwrap.fill(
            tarefa[2],
            width=90,
            subsequent_indent=" " * 4
    )

        texto = ctk.CTkLabel(
            tarefa_frame,
            justify="left",
            anchor="w",
            wraplength=700,
            font=("Segoe UI", 14),
            text=f"""

    Nome: {tarefa[1]}

    Descrição: {descricao_formatada}

    Prioridade: {tarefa[3]}

    Status: {tarefa[4]}

    Progresso: {tarefa[5]}% 
    """
)

        texto.pack(
            side="left",
            padx=20,
            pady=15
        )

        editar_btn = ctk.CTkButton(
            tarefa_frame,
            text="Editar",
            width=150,
            height=45,
            fg_color=PURPLE,
            hover_color=PURPLE_HOVER,
            font=("Segoe UI", 15, "bold"),
            command=lambda t=tarefa: abrir_opcoes_edicao(app, t)
        )

        editar_btn.pack(
            side="right",
            padx=20
        )


# Fun para escolher oque da tarefa o usuario quer editar
def abrir_opcoes_edicao(app, tarefa):

    # limpar tela
    for widget in app.winfo_children():
        widget.destroy()

    frame = ctk.CTkFrame(
        app,
        fg_color="transparent"
    )

    frame.pack(
        expand=True
    )
    voltar_btn = ctk.CTkButton(
        frame,
        text="← Voltar",
        width=120,
        height=40,
        fg_color= PURPLE,
        hover_color= PURPLE_HOVER,
        command=lambda:
        abrir_editar_task(app)
    )

    voltar_btn.pack(
        anchor="w",
        pady=(0, 20)
    )

    titulo = ctk.CTkLabel(
        frame,
        text=f"Editar: {tarefa[1]}",
        font=("Segoe UI", 30, "bold")
    )

    titulo.pack(
        pady=(20, 40)
    )

    opcoes = [

        ("Editar Tudo",
         lambda: editar_tudo(app, tarefa)),

        ("Editar Nome",
         lambda: editar_nome(app, tarefa)),

        ("Editar Descrição",
         lambda: editar_descricao(app, tarefa)),

        ("Editar Prioridade",
         lambda: editar_prioridade(app, tarefa)),

        ("Editar Status",
         lambda: editar_status(app, tarefa)),

        ("Editar Progresso",
         lambda: editar_progresso(app, tarefa))
    ]

    for texto, comando in opcoes:

        btn = ctk.CTkButton(
            frame,
            text=texto,
            width=320,
            height=55,
            fg_color=PURPLE,
            hover_color=PURPLE_HOVER,
            font=("Segoe UI", 16, "bold"),
            command=comando
        )

        btn.pack(pady=10)


# Tela base do código
def tela_base(app, titulo_texto):

    for widget in app.winfo_children():
        widget.destroy()

    frame = ctk.CTkFrame(
        app,
        fg_color="transparent"
    )

    frame.pack(
        expand=True,
        fill="both",
        padx=40,
        pady=30
    )

    # botão voltar
    voltar_btn = ctk.CTkButton(
        frame,
        text="← Voltar",
        width=120,
        height=40,
        fg_color= PURPLE,
        hover_color= PURPLE_HOVER,
        command=lambda:
            abrir_editar_task(app)
    )

    voltar_btn.pack(
        anchor="w",
        pady=(0, 20)
    )

    titulo = ctk.CTkLabel(
        frame,
        text=titulo_texto,
        font=("Segoe UI", 30, "bold")
    )

    titulo.pack(
        pady=(20, 30)
    )

    return frame



# opção editar tudo

def editar_tudo(app, tarefa):

    frame = tela_base(
        app,
        "Editar Tudo"
    )

    nome = ctk.CTkEntry(
        frame,
        height=50
    )

    nome.insert(
        0,
        tarefa[1]
    )

    nome.pack(fill="x", pady=10)

    descricao = ctk.CTkTextbox(
        frame,
        height=120
    )

    descricao.insert(
        "1.0",
        tarefa[2]
    )

    descricao.pack(fill="x", pady=10)

    prioridade = ctk.CTkOptionMenu(
        frame,
        values=[
            "Alta",
            "Média",
            "Baixa"
        ]
    )

    prioridade.set(
        tarefa[3]
    )

    prioridade.pack(fill="x", pady=10)

    status = ctk.CTkOptionMenu(
        frame,
        values=[
            "Não iniciada",
            "Em andamento",
            "Concluída"
        ]
    )

    status.set(
        tarefa[4]
    )

    status.pack(fill="x", pady=10)

    progresso = ctk.CTkSlider(
        frame,
        from_=0,
        to=100,
        number_of_steps=100
    )

    progresso.set(
        tarefa[5]
    )

    progresso.pack(fill="x", pady=20)

    def salvar():
        editar_tarefa(

            tarefa[0],
            nome.get(),
            descricao.get("1.0", "end").strip(),
            prioridade.get(),
            status.get(),
            int(progresso.get())
        )

        tela_sucesso_edicao(app, nome.get())


    btn = ctk.CTkButton(
        frame,
        text="Salvar",
        height=50,
        fg_color=PURPLE,
        hover_color=PURPLE_HOVER,
        command=salvar
    )

    btn.pack(pady=20)


# opção editar somente o nome
def editar_nome(app, tarefa):

    frame = tela_base(
        app,
        "Editar Nome"
    )

    entrada = ctk.CTkEntry(
        frame,
        height=50
    )

    entrada.insert(
        0,
        tarefa[1]
    )

    entrada.pack(fill="x", pady=20)

    def salvar():
        editar_tarefa(

            tarefa[0],
            entrada.get(),
            tarefa[2],
            tarefa[3],
            tarefa[4],
            tarefa[5]
        )

        tela_sucesso_edicao(app, tarefa[1])


    btn = ctk.CTkButton(
        frame,
        text="Salvar",
        height=50,
        fg_color=PURPLE,
        hover_color=PURPLE_HOVER,
        command=salvar
    )

    btn.pack(pady=20)


# opção editar somente a descrição
def editar_descricao(app, tarefa):

    frame = tela_base(
        app,
        "Editar Descrição"
    )

    entrada = ctk.CTkTextbox(
        frame,
        height=150
    )

    entrada.insert(
        "1.0",
        tarefa[2]
    )

    entrada.pack(fill="x", pady=20)

    def salvar():
        editar_tarefa(

            tarefa[0],
            tarefa[1],
            entrada.get("1.0", "end").strip(),
            tarefa[3],
            tarefa[4],
            tarefa[5]
        )

        
        tela_sucesso_edicao(app, tarefa[1])

    btn = ctk.CTkButton(
        frame,
        text="Salvar",
        height=50,
        fg_color=PURPLE,
        hover_color=PURPLE_HOVER,
        command=salvar
    )

    btn.pack(pady=20)


# opção editar somente a prioridade

def editar_prioridade(app, tarefa):

    frame = tela_base(
        app,
        "Editar Prioridade"
    )

    prioridade = ctk.CTkOptionMenu(
        frame,
        values=[
            "Alta",
            "Média",
            "Baixa"
        ]
    )

    prioridade.set(
        tarefa[3]
    )

    prioridade.pack(fill="x", pady=20)

    def salvar():
        editar_tarefa(

            tarefa[0],
            tarefa[1],
            tarefa[2],
            prioridade.get(),
            tarefa[4],
            tarefa[5]
        )

        tela_sucesso_edicao(app, tarefa[1])

    btn = ctk.CTkButton(
        frame,
        text="Salvar",
        height=50,
        fg_color=PURPLE,
        hover_color=PURPLE_HOVER,
        command=salvar
    )

    btn.pack(pady=20)


# opção editar status

def editar_status(app, tarefa):

    frame = tela_base(
        app,
        "Editar Status"
    )

    status = ctk.CTkOptionMenu(
        frame,
        values=[
            "Não iniciada",
            "Em andamento",
            "Concluída"
        ]
    )

    status.set(
        tarefa[4]
    )

    status.pack(fill="x", pady=20)

    def salvar():
        editar_tarefa(

            tarefa[0],
            tarefa[1],
            tarefa[2],
            tarefa[3],
            status.get(),
            tarefa[5]
        )

        tela_sucesso_edicao(app, tarefa[1])

    btn = ctk.CTkButton(
        frame,
        text="Salvar",
        height=50,
        fg_color=PURPLE,
        hover_color=PURPLE_HOVER,
        command=salvar
    )

    btn.pack(pady=20)


# opção editar progresso

def editar_progresso(app, tarefa):

    frame = tela_base(
        app,
        "Editar Progresso"
    )

    label = ctk.CTkLabel(
        frame,
        text=f"{tarefa[5]}%",
        font=("Segoe UI", 25, "bold")
    )

    label.pack(pady=10)

    progresso = ctk.CTkSlider(
        frame,
        from_=0,
        to=100,
        number_of_steps=100
    )

    progresso.set(
        tarefa[5]
    )

    progresso.pack(fill="x", pady=20)

    def atualizar(valor):

        label.configure(
            text=f"{int(valor)}%"
        )

    progresso.configure(
        command=atualizar
    )

    def salvar():
        editar_tarefa(

            tarefa[0],
            tarefa[1],
            tarefa[2],
            tarefa[3],
            tarefa[4],
            int(progresso.get())
        )

        tela_sucesso_edicao(app, tarefa[1])

    

    btn = ctk.CTkButton(
        frame,
        text="Salvar",
        height=50,
        fg_color=PURPLE,
        hover_color=PURPLE_HOVER,
        command=salvar
    )

    btn.pack(pady=20)
