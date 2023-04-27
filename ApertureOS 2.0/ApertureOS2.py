import tkinter as tk
from tkinter import ttk

def criar_janela_principal():
    # Cria a janela principal do desktop
    janela_principal = tk.Tk()
    janela_principal.title("ApertureOS v2.0")
    janela_principal.state("zoomed")
    # Configura a imagem de fundo centralizada
    imagem_fundo = tk.PhotoImage(file="assets/splash.png")
    label_imagem = tk.Label(janela_principal, image=imagem_fundo)
    label_imagem.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Cria os ícones clicáveis
    icone_calculadora = tk.PhotoImage(file="assets/calculator.png")
    botao_calculadora = tk.Button(janela_principal, image=icone_calculadora, command=abrir_calculadora)
    botao_calculadora.place(x=100, y=100)

    icone_editor_texto = tk.PhotoImage(file="assets/document.png")
    botao_editor_texto = tk.Button(janela_principal, image=icone_editor_texto, command=abrir_editor_texto)
    botao_editor_texto.place(x=300, y=100)

    icone_navegador = tk.PhotoImage(file="assets/ie.png")
    botao_navegador = tk.Button(janela_principal, image=icone_navegador, command=abrir_navegador)
    botao_navegador.place(x=500, y=100)

    icone_email = tk.PhotoImage(file="assets/folder.png")
    botao_email = tk.Button(janela_principal, image=icone_pasta, command=abrir_pasta)
    botao_email.place(x=700, y=100)

    # Inicia o loop de eventos da janela principal
    janela_principal.mainloop()

def fechar_splash():
    global splash
    splash.destroy()
    criar_janela_principal()

def abrir_calculadora():
    # Função a ser executada ao clicar no ícone da calculadora
    print("Abrindo a Calculadora")

def abrir_editor_texto():
    # Função a ser executada ao clicar no ícone do arquivo de texto
    print("Abrindo o Editor de Texto")

def abrir_navegador():
    # Função a ser executada ao clicar no ícone do navegador
    print("Abrindo o Navegador")

def abrir_pasta():
    # Função a ser executada ao clicar no ícone da pasta
    print("Abrindo Meus Documentos")

# Cria a janela de splash screen
splash = tk.Tk()
splash.title("Aperture OS v2.0")
splash.state("zoomed")

# Carrega a imagem
imagem = tk.PhotoImage(file="assets/splash.png")
# Redimensiona a imagem para a resolução desejada
imagem = imagem.subsample(4, 4)

# Adiciona um rótulo à splash screen com a imagem
rotulo_imagem = tk.Label(splash, image=imagem)
rotulo_imagem.pack(padx=50, pady=30)

# Cria uma barra de progresso
barra_progresso = ttk.Progressbar(splash, mode='indeterminate')
barra_progresso.pack(pady=10)

# Define a duração da splash screen (em milissegundos)
duracao_splash = 3000

# Configura o temporizador para fechar a splash screen após a conclusão da barra de progresso
splash.after(duracao_splash, fechar_splash)

# Inicia a barra de progresso
barra_progresso.start()

# Inicia o loop de eventos da splash screen
splash.mainloop()
