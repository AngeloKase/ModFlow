# =========================================
# ARQUIVO: ui/remove_task.py
# =========================================

import customtkinter as ctk
import textwrap


from database import (
    listar_tarefas,
    remover_tarefa
)

PURPLE = "#c77dff"
PURPLE_HOVER = "#a855f7"
GREEN = "#4ade80"

# =========================================
# VOLTAR MENU
# =========================================

def voltar_menu(app):

    from ui.menu import abrir_menu

    abrir_menu(app)


# =========================================
# ABRIR REMOVER
# =========================================

def abrir_remover_task(app):

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

    # botão voltar
    voltar_btn = ctk.CTkButton(
        frame,
        text="← Voltar",
        width=120,
        height=40,
        fg_color=PURPLE,
        hover_color=PURPLE_HOVER,
        command=lambda:
            voltar_menu(app)
    )

    voltar_btn.pack(
        anchor="w",
        pady=(0, 20)
    )

    # titulo
    titulo = ctk.CTkLabel(
        frame,
        text="Remover Tarefas",
        font=("Segoe UI", 32, "bold")
    )

    titulo.pack(
        pady=(0, 30)
    )

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
            subsequent_indent=" " * -1
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

        remover_btn = ctk.CTkButton(
            tarefa_frame,
            text="Remover",
            width=150,
            height=45,
            fg_color="#ef4444",
            hover_color="#dc2626",
            font=("Segoe UI", 15, "bold"),
            command=lambda t=tarefa:
                confirmar_remocao(app, t)
        )

        remover_btn.pack(
            side="right",
            padx=20
        )


# =========================================
# CONFIRMAR REMOÇÃO
# =========================================

# =========================================
# CONFIRMAR REMOÇÃO
# =========================================

# =========================================
# CONFIRMAR REMOÇÃO
# =========================================

def confirmar_remocao(app, tarefa):

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

    titulo = ctk.CTkLabel(
        frame,
        text="Confirmar Remoção",
        font=("Segoe UI", 30, "bold"),
        text_color="#ef4444"
    )

    titulo.pack(
        pady=(20, 30)
    )

    texto = ctk.CTkLabel(
        frame,
        text=f"""
Tem certeza que deseja remover:

{tarefa[1]} ?
""",
        font=("Segoe UI", 18)
    )

    texto.pack(
        pady=(0, 20)
    )

    # contador
    contador_label = ctk.CTkLabel(
        frame,
        text="Liberando em 5...",
        font=("Segoe UI", 16),
        text_color="#aaaaaa"
    )

    contador_label.pack(
        pady=(0, 20)
    )

    # frame dos botões
    botoes_frame = ctk.CTkFrame(
        frame,
        fg_color="transparent"
    )

    botoes_frame.pack()

    # botão remover
    sim_btn = ctk.CTkButton(
        botoes_frame,
        text="Aguarde...",
        width=180,
        height=50,
        state="disabled",
        fg_color="#ef4444",
        hover_color="#dc2626",
        font=("Segoe UI", 15, "bold"),
        command=lambda:
            remover(app, tarefa)
    )

    sim_btn.pack(
        side="left",
        padx=10
    )

    # botão cancelar
    nao_btn = ctk.CTkButton(
        botoes_frame,
        text="Cancelar",
        width=180,
        height=50,
        fg_color="#2a2a2a",
        hover_color="#3a3a3a",
        font=("Segoe UI", 15, "bold"),
        command=lambda:
            abrir_remover_task(app)
    )

    nao_btn.pack(
        side="left",
        padx=10
    )

    # =========================================
    # CONTAGEM
    # =========================================

    tempo = 5

    def atualizar_contagem():

        nonlocal tempo

        if tempo > 0:

            contador_label.configure(
                text=f"Liberando em {tempo}..."
            )

            tempo -= 1

            app.after(
                1000,
                atualizar_contagem
            )

        else:

            contador_label.configure(
                text="Agora você pode remover."
            )

            sim_btn.configure(
                state="normal",
                text="Sim, remover"
            )

    atualizar_contagem()


# =========================================
# REMOVER TAREFA
# =========================================

def remover(app, tarefa):

    remover_tarefa(
        tarefa[0]
    )

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

    titulo = ctk.CTkLabel(
        frame,
        text="Tarefa removida!",
        font=("Segoe UI", 32, "bold"),
        text_color=GREEN,
    )
    titulo.pack(
        pady=(20, 20)
    )

    subtitulo = ctk.CTkLabel(
        frame,
        text=f'"{tarefa[1]}" foi removida do sistema.',
        font=("Segoe UI", 18)
    )

    subtitulo.pack(
        pady=(0, 30)
    )

    voltar_btn = ctk.CTkButton(
        frame,
        text="Voltar",
        width=250,
        height=55,
        fg_color=PURPLE,
        hover_color=PURPLE_HOVER,
        font=("Segoe UI", 16, "bold"),
        command=lambda:
            abrir_remover_task(app)
    )

    voltar_btn.pack()