import tkinter as tk
from tkinter import *

class Principal:
    def __init__(self, master=None):
        self.janela = Frame(master)
        self.fontePadrao = ("Arial", "12")
        self.janela.pack()

        self.titulo = Label(self.janela, text="Página Inicial")
        self.titulo["font"] = ("Arial", "29", "bold")
        self.titulo.pack()

        self.janela2 = Frame(master)
        self.janela2["padx"] = 20
        self.janela2.pack()

        self.janela3 = Frame(master)
        self.janela3["padx"] = 20
        self.janela3.pack()

        self.janela4 = Frame(master)
        self.janela4["padx"] = 20
        self.janela4.pack()

        self.janela5 = Frame(master)
        self.janela5["padx"] = 20
        self.janela5.pack()

        # Criar e empacotar os botões
        self.btnUsuario = Button(self.janela2, text="Usuário", font=("Calibri", "8"), width=12, command=self.verificarSenha)
        self.btnUsuario.pack()

        self.btnCidades = Button(self.janela2, text="Cidades", font=("Calibri", "8"), width=12, command=self.verificarSenha)
        self.btnCidades.pack()

        self.btnClientes = Button(self.janela2, text="Clientes", font=("Calibri", "8"), width=12, command=self.verificarSenha)
        self.btnClientes.pack()

        self.btnFechar = Button(self.janela2, text="Fechar", font=("Calibri", "8"), width=12, command=self.verificarSenha)
        self.btnFechar.pack(side=LEFT)

        self.mensagem = Label(self.janela4, text="", font=self.fontePadrao)
        self.mensagem.pack()

        # Adicionar campos de entrada para usuário e senha
        self.lblNome = Label(self.janela3, text="Usuário:", font=self.fontePadrao)
        self.lblNome.pack()
        self.nome = Entry(self.janela3, font=self.fontePadrao)
        self.nome.pack()

        self.lblSenha = Label(self.janela3, text="Senha:", font=self.fontePadrao)
        self.lblSenha.pack()
        self.senha = Entry(self.janela3, show="*", font=self.fontePadrao)
        self.senha.pack()

    def verificarSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "usuarioSenai" and senha == "123456":
            self.mensagem["text"] = "Autenticado"
        else:
            self.mensagem["text"] = "Erro na autenticação"

# Execução da interface
if __name__ == "__main__":
    root = Tk()
    app = Principal(root)
    root.mainloop()