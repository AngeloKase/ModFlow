import customtkinter as ctk
from PIL import Image
from ui.menu import abrir_menu

# Configurando o tema da janela

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")





# Cores


BG_COLOR = ("#f5f5f5", "#111111")
CARD_COLOR = ("#ffffff", "#181818")
TEXT_COLOR = ("#111111", "#ffffff")
SECOND_TEXT = ("#555555", "#aaaaaa")

PURPLE = "#c77dff"
PURPLE_HOVER = "#a855f7"

# Janela principal


app = ctk.CTk()

app.title("ModFlow")
app.geometry("1200x800")

# fullscreen
app.attributes("-fullscreen", True)

app.configure(
    fg_color=BG_COLOR
)


# Colocando para o programa abrir em tela cheia

fullscreen = True

# Fazendo dois metodos para poder entrar e sair da tela cheia

def sair_fullscreen(event=None):

    global fullscreen

    fullscreen = False

    app.attributes(
        "-fullscreen",
        False
    )


def entrar_fullscreen(event=None):

    global fullscreen

    fullscreen = True

    app.attributes(
        "-fullscreen",
        True
    )


# Colocando os comandos para a função

# ESC sai da tela cheia

app.bind(
    "<Escape>",
    sair_fullscreen
)

# F11 entra em tela cheia

app.bind(
    "<F11>",
    entrar_fullscreen
)



# colocando o tema base do código escuro

modo_atual = "dark"

# Função para trocar o tema
 
def trocar_tema():

    global modo_atual

    if modo_atual == "dark":

        ctk.set_appearance_mode("light")

        tema_btn.configure(
            text="☀"
        )

        modo_atual = "light"

    else:

        ctk.set_appearance_mode("dark")

        tema_btn.configure(
            text="🌙"
        )

        modo_atual = "dark"


def sair_fullscreen(event):

    app.attributes(
        "-fullscreen",
        False
    )


# ESC para sair do fullscreen

app.bind(
    "<Escape>",
    sair_fullscreen
)

# Frame central

frame = ctk.CTkFrame(
    app,
    width=700,
    height=700,
    corner_radius=25,
    fg_color=CARD_COLOR,
    border_width=2,
    border_color=PURPLE
)

frame.place(
    relx=0.5,
    rely=0.5,
    anchor="center"
)

# impedir resize automático

frame.pack_propagate(False)

# botão para mudar o tema

tema_btn = ctk.CTkButton(
    frame,
    text="🌙",
    width=45,
    height=45,
    corner_radius=100,
    fg_color=PURPLE,
    hover_color=PURPLE_HOVER,
    font=("Segoe UI", 18),
    command=trocar_tema
)

tema_btn.place(
    relx=0.92,
    rely=0.05,
    anchor="center"
)

# Colocando a logo

imagem = ctk.CTkImage(
    light_image=Image.open(
        "assets/server_icon.png"
    ),
    dark_image=Image.open(
        "assets/server_icon.png"
    ),
    size=(480, 300)
)

logo = ctk.CTkLabel(
    frame,
    image=imagem,
    text=""
)

logo.pack(
    pady=(40, 20)
)


titulo = ctk.CTkLabel(
    frame,
    text="ModFlow",
    font=("Segoe UI", 42, "bold"),
    text_color=TEXT_COLOR
)

titulo.pack()

descricao = ctk.CTkLabel(
    frame,
    text="Painel de gerenciamento de tarefas para moderadores do Discord",
    font=("Segoe UI", 16),
    text_color=SECOND_TEXT
)

descricao.pack(
    pady=(10, 40)
)

botao_comecar = ctk.CTkButton(
    frame,
    text="Começar",
    width=260,
    height=60,
    corner_radius=20,
    fg_color=PURPLE,
    hover_color=PURPLE_HOVER,
    font=("Segoe UI", 18, "bold"),
    command=lambda:
        abrir_menu(app)
)

botao_comecar.pack()


footer = ctk.CTkLabel(
    frame,
    text="ModFlow © 2026",
    font=("Segoe UI", 12),
    text_color=SECOND_TEXT
)

footer.pack(
    side="bottom",
    pady=20
)
app.mainloop()
