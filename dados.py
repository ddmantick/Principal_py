import tkinter as tk
from tkinter import *

class Login:
    def __init__(self, master=None):
        self.janela = Frame(master)
        self.fontePadrao = ("Arial", "12")
        self.janela.pack()

        self.titulo = Label(self.janela, text="Informe os dados")
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

        self.janela6 = Frame(master)
        self.janela6["padx"] = 20
        self.janela6.pack()

        self.janela7 = Frame(master)
        self.janela7["padx"] = 20
        self.janela7.pack()

        self.janela8 = Frame(master)
        self.janela8["padx"] = 20
        self.janela8.pack()

        self.nomeLabel = Label(self.janela2, text="ID Usuário", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)
        self.nome = Entry(self.janela2)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.btnBuscar = Button(self.janela2)
        self.btnBuscar["text"] = "Buscar"
        self.btnBuscar["font"] = ("Calibri", "8")
        self.btnBuscar["width"] = 12
        self.btnBuscar["command"] = self.buscarUsuario
        self.btnBuscar.pack()

        self.senhaLabel = Label(self.janela3, text="Nome", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)
        self.senha = Entry(self.janela3)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha.pack(side=LEFT)

        self.numeroLabel = Label(self.janela4, text="Telefone", font=self.fontePadrao)
        self.numeroLabel.pack(side=LEFT)
        self.numero = Entry(self.janela4)
        self.numero["width"] = 30
        self.numero["font"] = self.fontePadrao
        self.numero.pack(side=LEFT)

        self.emailLabel = Label(self.janela5, text="E-mail", font=self.fontePadrao)
        self.emailLabel.pack(side=LEFT)
        self.email = Entry(self.janela5)
        self.email["width"] = 30
        self.email["font"] = self.fontePadrao
        self.email.pack(side=LEFT)

        self.usuarioLabel = Label(self.janela6, text="Usuário", font=self.fontePadrao)
        self.usuarioLabel.pack(side=LEFT)
        self.usuario = Entry(self.janela6)
        self.usuario["width"] = 30
        self.usuario["font"] = self.fontePadrao
        self.usuario.pack(side=LEFT)

        self.senhaLabel = Label(self.janela7, text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)
        self.senha = Entry(self.janela7, show="*")
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha.pack(side=LEFT)

        self.bntInsert = Button(self.janela8)
        self.bntInsert["text"] = "Inserir"
        self.bntInsert["font"] = ("Calibri", "8")
        self.bntInsert["width"] = 20
        self.bntInsert["command"] = self.inserirUsuario
        self.bntInsert.pack()

        self.bntAlterar = Button(self.janela8)
        self.bntAlterar["text"] = "Alterar"
        self.bntAlterar["font"] = ("Calibri", "8")
        self.bntAlterar["width"] = 20
        self.bntAlterar["command"] = self.alterarUsuario
        self.bntAlterar.pack()

        self.bntExcluir = Button(self.janela8)
        self.bntExcluir["text"] = "Excluir"
        self.bntExcluir["font"] = ("Calibri", "8")
        self.bntExcluir["width"] = 20
        self.bntExcluir["command"] = self.excluirUsuario
        self.bntExcluir.pack()

        self.mensagem = Label(self.janela4, text="", font=self.fontePadrao)
        self.mensagem.pack()

    def bnt(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "usuarioSenai" and senha == "123456":
            self.mensagem["text"] = "Autenticado"
        else:
            self.mensagem["text"] = "Erro na autenticação"

    def buscarUsuario(self):
        user = Usuario()
        idusuario = self.nome.get()
        self.mensagem["text"] = user.selectUser(idusuario)
        self.nome.delete(0, END)
        self.senha.delete(0, END)
        self.numero.delete(0, END)
        self.email.delete(0, END)
        self.usuario.delete(0, END)

    def inserirUsuario(self):
        user = Usuario()
        user.nome = self.senha.get()
        user.telefone = self.numero.get()
        user.email = self.email.get()
        user.usuario = self.usuario.get()
        user.senha = self.senha.get()
        self.mensagem["text"] = user.insertUser()
        self.nome.delete(0, END)
        self.senha.delete(0, END)
        self.numero.delete(0, END)
        self.email.delete(0, END)
        self.usuario.delete(0, END)

    def alterarUsuario(self):
        user = Usuario()
        user.idusuario = self.nome.get()
        user.nome = self.senha.get()
        user.telefone = self.numero.get()
        user.email = self.email.get()
        user.usuario = self.usuario.get()
        user.senha = self.senha.get()
        self.mensagem["text"] = user.updateUser()
        self.nome.delete(0, END)
        self.senha.delete(0, END)
        self.numero.delete(0, END)
        self.email.delete(0, END)
        self.usuario.delete(0, END)

    def excluirUsuario(self):
        user = Usuario()
        user.idusuario = self.nome.get()
        self.mensagem["text"] = user.deleteUser()
        self.nome.delete(0, END)
        self.senha.delete(0, END)
        self.numero.delete(0, END)
        self.email.delete(0, END)
        self.usuario.delete(0, END)

root = Tk()
Login(root)
root.mainloop()