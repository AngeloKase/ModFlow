import customtkinter as ctk

from ui.add_task import abrir_add_task
from ui.tasks import abrir_ver_tarefas
from ui.edit_task import abrir_editar_task
from ui.remove_task import abrir_remover_task

PURPLE = "#c77dff"


def abrir_menu(app):

    # limpa a tela atual
    for widget in app.winfo_children():
        widget.destroy()

    # =========================================
    # FRAME CENTRAL
    # =========================================

    frame = ctk.CTkFrame(
        app,
        width=700,
        height=650,
        corner_radius=25,
        fg_color=("white", "#181818"),
        border_width=2,
        border_color=PURPLE
    )

    frame.place(
        relx=0.5,
        rely=0.5,
        anchor="center"
    )

    frame.pack_propagate(False)

    # =========================================
    # BOTÃO TEMA
    # =========================================

    def trocar_tema():

        modo = ctk.get_appearance_mode()

        if modo == "Dark":

            ctk.set_appearance_mode("light")

            tema_btn.configure(
                text="☀"
            )

        else:

            ctk.set_appearance_mode("dark")

            tema_btn.configure(
                text="🌙"
            )

    tema_btn = ctk.CTkButton(
        frame,
        text="🌙",
        width=45,
        height=45,
        corner_radius=100,
        fg_color=PURPLE,
        hover_color="#a855f7",
        font=("Segoe UI", 18),
        command=trocar_tema
    )

    tema_btn.place(
        relx=0.92,
        rely=0.05,
        anchor="center"
    )

    # =========================================
    # TITULO
    # =========================================

    titulo = ctk.CTkLabel(
        frame,
        text="Menu Principal",
        font=("Segoe UI", 38, "bold"),
        text_color=("black", "white")
    )

    titulo.pack(
        pady=(70, 15)
    )

    # =========================================
    # DESCRIÇÃO
    # =========================================

    descricao = ctk.CTkLabel(
        frame,
        text="Gerencie tarefas da moderação de forma rápida e organizada",
        font=("Segoe UI", 16),
        text_color=("#555555", "#aaaaaa")
    )

    descricao.pack(
        pady=(0, 40)
    )

    # =========================================
    # BOTÕES
    # =========================================

    botoes = [

        ("Adicionar Tarefa",
         lambda: abrir_add_task(app)),

        ("Editar Tarefa",
         lambda: abrir_editar_task(app)),

        ("Remover Tarefa",
         lambda: abrir_remover_task(app)),

        ("Ver Tarefas",
         lambda: abrir_ver_tarefas(app))
    ]

    for texto, comando in botoes:

        botao = ctk.CTkButton(
            frame,
            text=texto,
            width=320,
            height=60,
            corner_radius=18,
            fg_color=PURPLE,
            hover_color="#a855f7",
            font=("Segoe UI", 18, "bold"),
            command=comando
        )

        botao.pack(
            pady=12
        )

    # =========================================
    # FOOTER
    # =========================================

    footer = ctk.CTkLabel(
        frame,
        text="ModFlow © 2026",
        font=("Segoe UI", 12),
        text_color=("#666666", "#888888")
    )

    footer.pack(
        side="bottom",
        pady=20
    )
