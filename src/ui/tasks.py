import customtkinter as ctk
from database import listar_tarefas

PURPLE = "#c77dff"


def voltar_menu(app):
    from ui.menu import abrir_menu
    abrir_menu(app)


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
        fg_color="#2a2a2a",
        hover_color="#3a3a3a",
        command=lambda: voltar_menu(app)
    )
    voltar_btn.pack(side="left")

    titulo = ctk.CTkLabel(
        frame,
        text="Minhas Tarefas",
        font=("Segoe UI", 32, "bold"),
        text_color="white"
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
            text_color="gray"
        )
        vazio.pack(pady=40)
        return

    # cards das tarefas
    for t in tarefas:
        # esperado: (id, nome, descricao, prioridade, status, porcentagem)
        id, nome, descricao, prioridade, status, progresso = t

        card = ctk.CTkFrame(
            scroll,
            fg_color="#1e1e1e",
            corner_radius=15
        )
        card.pack(fill="x", pady=10)

        # título
        titulo = ctk.CTkLabel(
            card,
            text=f"{nome}",
            font=("Segoe UI", 20, "bold"),
            text_color="white"
        )
        titulo.pack(anchor="w", padx=15, pady=(10, 0))

        # descrição
        desc = ctk.CTkLabel(
            card,
            text=descricao[:120] + "",
            font=("Segoe UI", 13),
            text_color="gray"
        )
        desc.pack(anchor="w", padx=15)

        # info linha
        info = ctk.CTkLabel(
            card,
            text=f"Prioridade: {prioridade} | Status: {status}",
            font=("Segoe UI", 13),
            text_color="#c77dff"
        )
        info.pack(anchor="w", padx=15, pady=(5, 0))

        # progresso
        barra = ctk.CTkProgressBar(card)
        barra.set(progresso / 100)
        barra.pack(fill="x", padx=15, pady=(10, 15))