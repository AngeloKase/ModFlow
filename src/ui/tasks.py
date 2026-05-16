import customtkinter as ctk
from database import listar_tarefas

CARD_COLOR = ("#ffffff", "#181818")
TEXT_COLOR = ("#111111", "#ffffff")
SECOND_TEXT = ("#555555", "#aaaaaa")

PURPLE = "#c77dff"
PURPLE_HOVER = "#a855f7"


def voltar_menu(app):
    from ui.menu import abrir_menu
    abrir_menu(app)


# fun ver mais da tarefa
def abrir_detalhes_tarefa(
    app,
    id_tarefa,
    nome,
    descricao,
    prioridade,
    status,
    progresso
):

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

    top = ctk.CTkFrame(
        frame,
        fg_color="transparent"
    )

    top.pack(fill="x")

    voltar_btn = ctk.CTkButton(
        top,
        text="← Voltar",
        width=120,
        height=40,
        fg_color=PURPLE,
        hover_color=PURPLE_HOVER,
        command=lambda:
            abrir_ver_tarefas(app)
    )

    voltar_btn.pack(side="left")

    titulo = ctk.CTkLabel(
        frame,
        text=nome,
        font=("Segoe UI", 32, "bold"),
        text_color=TEXT_COLOR
    )

    titulo.pack(
        anchor="w",
        pady=(25, 20)
    )

    info = ctk.CTkLabel(
        frame,
        text=f"Prioridade: {prioridade} | Status: {status}",
        font=("Segoe UI", 15, "bold"),
        text_color=PURPLE
    )

    info.pack(anchor="w")

    progresso_label = ctk.CTkLabel(
        frame,
        text=f"Progresso: {progresso}%",
        font=("Segoe UI", 14),
        text_color=TEXT_COLOR
    )

    progresso_label.pack(
        anchor="w",
        pady=(20, 10)
    )

    barra = ctk.CTkProgressBar(frame)

    barra.set(
        progresso / 100
    )

    barra.pack(
        fill="x",
        pady=(0, 25)
    )

    descricao_box = ctk.CTkFrame(
        frame,
        fg_color=CARD_COLOR,
        corner_radius=15
    )

    descricao_box.pack(
        fill="both",
        expand=True
    )

    descricao_titulo = ctk.CTkLabel(
        descricao_box,
        text="Descrição",
        font=("Segoe UI", 22, "bold"),
        text_color=TEXT_COLOR
    )

    descricao_titulo.pack(
        anchor="w",
        padx=20,
        pady=(20, 10)
    )

    descricao_label = ctk.CTkLabel(
        descricao_box,
        text=descricao,
        justify="left",
        wraplength=900,
        font=("Segoe UI", 15),
        text_color=TEXT_COLOR
    )

    descricao_label.pack(
        anchor="w",
        padx=20,
        pady=(0, 20)
    )


def abrir_ver_tarefas(app):

    
    for widget in app.winfo_children():
        widget.destroy()

    
    frame = ctk.CTkFrame(app, fg_color="transparent")
    frame.pack(expand=True, fill="both", padx=40, pady=30)

    
    top = ctk.CTkFrame(frame, fg_color="transparent")
    top.pack(fill="x")

    voltar_btn = ctk.CTkButton(
        top,
        text="← Voltar",
        width=120,
        height=40,
        fg_color=PURPLE,
        hover_color=PURPLE_HOVER,
        command=lambda: voltar_menu(app)
    )

    voltar_btn.pack(side="left")

    titulo = ctk.CTkLabel(
        frame,
        text="Minhas Tarefas",
        font=("Segoe UI", 32, "bold"),
        text_color=TEXT_COLOR
    )

    titulo.pack(pady=(20, 20))

    # area de scroll para ver todas as tarefas
    scroll = ctk.CTkScrollableFrame(frame, fg_color="transparent")
    scroll.pack(fill="both", expand=True)

    tarefas = listar_tarefas()

    if not tarefas:
        vazio = ctk.CTkLabel(
            scroll,
            text="Nenhuma tarefa encontrada 😴",
            font=("Segoe UI", 18),
            text_color=SECOND_TEXT
        )
        vazio.pack(pady=40)
        return

    # cards das tarefas
    for t in tarefas:
        # esperado: (id, nome, descricao, prioridade, status, porcentagem)
        id, nome, descricao, prioridade, status, progresso = t

        card = ctk.CTkFrame(
            scroll,
            fg_color=CARD_COLOR,
            corner_radius=15
        )

        card.pack(fill="x", pady=10)

        # cabeçalho

        header = ctk.CTkFrame(
            card,
            fg_color="transparent"
        )

        header.pack(
            fill="x",
            padx=15,
            pady=(15, 5)
        )

        
        titulo = ctk.CTkLabel(
            header,
            text=f"{nome}",
            font=("Segoe UI", 20, "bold"),
            text_color=TEXT_COLOR
        )

        titulo.pack(side="left")

        # botão detalhes
        detalhes_btn = ctk.CTkButton(
            header,
            text="Detalhes",
            width=95,
            height=32,
            corner_radius=10,
            fg_color=PURPLE,
            hover_color=PURPLE_HOVER,
            font=("Segoe UI", 12, "bold"),
            command=lambda
                i=id,
                n=nome,
                d=descricao,
                p=prioridade,
                s=status,
                prog=progresso:
                    abrir_detalhes_tarefa(
                        app,
                        i,
                        n,
                        d,
                        p,
                        s,
                        prog
                    )
        )

        detalhes_btn.pack(side="right")

        # descrição
        desc = ctk.CTkLabel(
            card,
            text=(descricao[:120] + "...") if len(descricao) > 120 else descricao,
            font=("Segoe UI", 13),
            text_color=SECOND_TEXT,
            wraplength=700,
            justify="left"
        )

        desc.pack(anchor="w", padx=15)

        # info linha
        info = ctk.CTkLabel(
            card,
            text=f"Prioridade: {prioridade} | Status: {status}",
            font=("Segoe UI", 13),
            text_color=PURPLE
        )

        info.pack(anchor="w", padx=15, pady=(5, 0))

        # progresso
        barra = ctk.CTkProgressBar(card)

        barra.set(progresso / 100)

        barra.pack(fill="x", padx=15, pady=(10, 15))
