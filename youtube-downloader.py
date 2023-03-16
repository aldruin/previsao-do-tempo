'''@author - aldruinn
o código propoe uma janela simples em que o usuário pode inserir uma URL do YouTube para ter o video baixado'''


import tkinter as tk
import threading
from tkinter import messagebox, Button, Entry, Label
from pytube import YouTube

# Função para baixar o vídeo MP4
def baixar_mp4():
    url = entrada_url.get()
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    stream.download()
    messagebox.showinfo('Concluído', 'Download concluído com sucesso!')

# Função que cria uma nova thread para executar a função baixar_mp4
def baixar_mp4_thread():
    t = threading.Thread(target=baixar_mp4)
    t.start()
    messagebox.showinfo('Em andamento...', 'Download em andamento...')

# Função que define o autor do programa
def set_autor():
    lb_autor = Label(janela, text="@aldruinn")
    lb_autor.grid(row=2, column=1, pady=10)

# Cria a janela principal
janela = tk.Tk()
janela.title('Download Tube')
janela.geometry('300x100')

# Cria um campo para o usuário inserir a URL
lb_url = Label(janela, text='URL:')
lb_url.grid(row=0, column=0, padx=5, pady=5)
entrada_url = Entry(janela)
entrada_url.grid(row=0, column=1, padx=5, pady=5)

# Cria um botão para o usuário iniciar o download
botao = Button(janela, text="Baixar", command=baixar_mp4_thread)
botao.grid(row=0, column=2, padx=5, pady=5)

# Cria um label para exibir o autor do programa
botao_autor = Button(janela, text="Autor", command=set_autor)
botao_autor.grid(row=2, column=0, padx=1, pady=1)

# Inicia a janela principal
janela.mainloop()
