import customtkinter as ctk
from database import adicionar_tarefa

TEXT_COLOR = ("#111111", "#ffffff")
SECOND_TEXT = ("#555555", "#aaaaaa")

PURPLE = "#c77dff"
PURPLE_HOVER = "#a855f7"
GREEN = "#4ade80"

# fun para voltar para o menu

def voltar_menu(app):

    from ui.menu import abrir_menu

    abrir_menu(app)


def abrir_add_task(app):

    
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

    
    top_frame = ctk.CTkFrame(
        frame,
        fg_color="transparent"
    )

    top_frame.pack(fill="x")

    voltar_btn = ctk.CTkButton(
        top_frame,
        text="← Voltar",
        width=120,
        height=40,
        fg_color= PURPLE,
        hover_color= PURPLE_HOVER,
        command=lambda: voltar_menu(app)
    )

    voltar_btn.pack(side="left")

    # titulo de adicionar a tarefa
    titulo = ctk.CTkLabel(
        frame,
        text="Adicionar Tarefa",
        font=("Segoe UI", 32, "bold"),
        text_color=TEXT_COLOR
    )

    titulo.pack(pady=(20, 30))

    # caixa de entrada para nome
    nome_entry = ctk.CTkEntry(
        frame,
        placeholder_text="Nome da tarefa",
        height=50,
        font=("Segoe UI", 15)
    )

    nome_entry.pack(fill="x", pady=10)

    # descricao da tarefa
    descricao_entry = ctk.CTkTextbox(
        frame,
        height=100,
        font=("Segoe UI", 14),
    )

    descricao_entry.pack(fill="x", pady=10)

    # exemplo de preenchimento para indicar oque se deve escrever
    placeholder = "Descrição da tarefa..."

    descricao_entry.insert("1.0", placeholder)

    def remover_placeholder(event):
        if descricao_entry.get("1.0", "end-1c") == placeholder:
            descricao_entry.delete("1.0", "end")
            descricao_entry.configure(text_color=SECOND_TEXT)

    def adicionar_placeholder(event):
        if descricao_entry.get("1.0", "end-1c").strip() == "":
            descricao_entry.insert("1.0", placeholder)
            descricao_entry.configure(text_color=SECOND_TEXT)

    descricao_entry.bind("<FocusIn>", remover_placeholder)
    descricao_entry.bind("<FocusOut>", adicionar_placeholder)

    # prioridade da tarefa
    prioridade_label = ctk.CTkLabel(
        frame,
        text="Prioridade",
        font=("Segoe UI", 15, "bold")
    )

    prioridade_label.pack(anchor="w", pady=(15, 5))

    prioridade = ctk.CTkOptionMenu(
        frame,
        values=["Alta", "Média", "Baixa"]
    )

    prioridade.pack(fill="x")

    # status da tarefa
    status_label = ctk.CTkLabel(
        frame,
        text="Status",
        font=("Segoe UI", 15, "bold")
    )

    status_label.pack(anchor="w", pady=(15, 5))

    status = ctk.CTkOptionMenu(
        frame,
        values=[
            "Não iniciada",
            "Em andamento",
            "Concluída"
        ]
    )

    status.pack(fill="x")

    # porcentagem de conclusao da tarefa
    porcentagem_frame = ctk.CTkFrame(
        frame,
        fg_color="transparent"
    )

    porcentagem_frame.pack(
        fill="x",
        pady=20
    )

    porcentagem_titulo = ctk.CTkLabel(
        porcentagem_frame,
        text="Progresso da tarefa",
        font=("Segoe UI", 15, "bold")
    )

    porcentagem_titulo.pack(anchor="w")

    porcentagem_label = ctk.CTkLabel(
        porcentagem_frame,
        text="50%",
        font=("Segoe UI", 22, "bold"),
        text_color=PURPLE
    )

    porcentagem_label.pack(
        pady=10
    )

    porcentagem = ctk.CTkSlider(
        porcentagem_frame,
        from_=0,
        to=100,
        number_of_steps=100
    )

    porcentagem.pack(fill="x")

    # Atualizar porcentagem
    def atualizar_porcentagem(valor):

        porcentagem_label.configure(
            text=f"{int(valor)}%"
        )

    porcentagem.configure(
        command=atualizar_porcentagem
    )

    # fun salvar tarefa
    def salvar():

        nome = nome_entry.get()

        descricao = descricao_entry.get("1.0", "end")

        adicionar_tarefa(
            nome,
            descricao,
            prioridade.get(),
            status.get(),
            int(porcentagem.get())
        )

        # tela de concluido com sucesso

        for widget in app.winfo_children():
            widget.destroy()

        sucesso_frame = ctk.CTkFrame(
            app,
            fg_color="transparent"
        )

        sucesso_frame.pack(expand=True)

        titulo_sucesso = ctk.CTkLabel(
            sucesso_frame,
            text="Tarefa salva com sucesso!",
            font=("Segoe UI", 34, "bold"),
            text_color= GREEN
        )

        titulo_sucesso.pack(
            pady=(20, 15)
        )

        subtitulo = ctk.CTkLabel(
            sucesso_frame,
            text=f'"{nome}" foi adicionada ao sistema.',
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
            hover_color= PURPLE_HOVER,
            font=("Segoe UI", 17, "bold"),
            command=lambda: voltar_menu(app)
        )

        voltar_menu_btn.pack()

    # botao para salvar
    salvar_btn = ctk.CTkButton(
        frame,
        text="Salvar Tarefa",
        height=55,
        fg_color=PURPLE,
        hover_color= PURPLE_HOVER,
        font=("Segoe UI", 17, "bold"),
        command=salvar
    )

    salvar_btn.pack(
        fill="x",
        pady=30
    )
