import customtkinter as ctk
from ui.add_task import abrir_add_task
from ui.tasks import abrir_ver_tarefas

PURPLE = "#c77dff"
BG_COLOR = "#121212"


def abrir_menu(app):

    # limpa a tela atual
    for widget in app.winfo_children():
        widget.destroy()

    frame = ctk.CTkFrame(
        app,
        fg_color="transparent"
    )

    frame.pack(expand=True)

    # titulo do menu
    titulo = ctk.CTkLabel(
        frame,
        text="Menu Principal",
        font=("Segoe UI", 35, "bold"),
        text_color="#FFFFFF"
    )

    titulo.pack(pady=(20, 40))

    # os botoes das possibilidades
    botoes = [
        ("Adicionar Tarefa", lambda: abrir_add_task(app)),
        ("Editar Tarefa", lambda: print("Editar")),
        ("Remover Tarefa", lambda: print("Remover")),
        ("Ver Tarefas", lambda: abrir_ver_tarefas(app))
    ]

    for texto, comando in botoes:

        botao = ctk.CTkButton(
            frame,
            text=texto,
            width=300,
            height=55,
            corner_radius=15,
            fg_color=PURPLE,
            hover_color="#a855f7",
            font=("Segoe UI", 18, "bold"),
            command=comando
        )

        botao.pack(pady=10)