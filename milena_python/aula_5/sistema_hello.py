#desenha tela GUI
import tkinter as tk
from tkinter import messagebox

#exibir nome da pessoa
def mostrar_mensagem():
    nome = entrada_nome.get()
    messagebox.showinfo('Saudação', f'Olá, {nome}. Bem vindo(a)!')

#criar janela
janela = tk.Tk()
janela.title('Olá, Tkinter')
janela.geometry('300x150')

#criar label do input
rotulo_nome = tk.Label(janela, text='Digite seu nome:', bg='lightblue')
rotulo_nome.pack(pady=5) #configurando estilo do texto

#criando campo de texto
entrada_nome = tk.Entry(janela)
entrada_nome.pack(pady=20)

botao = tk.Button(janela, text='Clique aqui', command=mostrar_mensagem, bg='lightblue')
botao.pack(pady=20)

#inicia o tk
janela.mainloop()