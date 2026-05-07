import customtkinter as ctk
from PIL import Image
from ui.menu import abrir_menu

# tema da janela
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# Janela principal
app = ctk.CTk()

app.title("ModFlow")
app.geometry("1200x800")
app.resizable(True, True)


# cores utilizadas

BG_COLOR = "#121212"
PURPLE = "#c77dff"

app.configure(fg_color=BG_COLOR)

# frame principal 

frame = ctk.CTkFrame(
    app,
    fg_color="transparent"
)

frame.pack(expand=True)

# icone do nosso servidor
imagem = ctk.CTkImage(
    light_image=Image.open("assets/server_icon.png"),
    dark_image=Image.open("assets/server_icon.png"),
    size=(150, 150)
)

logo = ctk.CTkLabel(
    frame,
    image=imagem,
    text=""
)

logo.pack(pady=(20, 10))

# titulo do aplicativo

titulo = ctk.CTkLabel(
    frame,
    text="ModFlow",
    font=("Segoe UI", 40, "bold"),
    text_color="white"
)

titulo.pack(pady=(10, 5))

# descrevendo o app
descricao = ctk.CTkLabel(
    frame,
    text="Painel de gerenciamento de tarefas para moderadores do Discord",
    font=("Segoe UI", 16),
    text_color="#aaaaaa"
)

descricao.pack(pady=(0, 30))

# botao para comecar
botao_comecar = ctk.CTkButton(
    frame,
    text="Começar",
    width=220,
    height=50,
    corner_radius=15,
    fg_color=PURPLE,
    hover_color="#acd855f7",
    font=("Segoe UI", 18, "bold"),
    command=lambda: abrir_menu(app)
)

botao_comecar.pack()

# Rodar app
app.mainloop()
