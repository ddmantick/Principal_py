import tkinter as tk

class Login:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Login")

        self.fontePadrao = ("Arial", "12")

        # Configuração da janela principal
        self.janela = tk.Frame(master)
        self.janela.pack(padx=20, pady=20)

        self.titulo = tk.Label(self.janela, text="Informe os dados")
        self.titulo["font"] = ("Arial", "29", "bold")
        self.titulo.pack(pady=10)

        # Frame para o campo de ID de usuário e botão buscar
        self.janela2 = tk.Frame(self.janela)
        self.janela2.pack(pady=5)

        self.nomeLabel = tk.Label(self.janela2, text="ID Usuário", font=self.fontePadrao)
        self.nomeLabel.pack(side=tk.LEFT)

        self.nome = tk.Entry(self.janela2, width=30, font=self.fontePadrao)
        self.nome.pack(side=tk.LEFT)

        self.buscar = tk.Button(self.janela2, text="Buscar", font=("Calibri", "8"), width=12, command=self.verificarSenha)
        self.buscar.pack(side=tk.LEFT)

        # Frame para o campo de Nome
        self.janela3 = tk.Frame(self.janela)
        self.janela3.pack(pady=5)

        self.nomeLabel = tk.Label(self.janela3, text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=tk.LEFT)

        self.nomeEntry = tk.Entry(self.janela3, width=30, font=self.fontePadrao)
        self.nomeEntry.pack(side=tk.LEFT)

        # Frame para o campo de Telefone
        self.janela4 = tk.Frame(self.janela)
        self.janela4.pack(pady=5)

        self.telefoneLabel = tk.Label(self.janela4, text="Telefone", font=self.fontePadrao)
        self.telefoneLabel.pack(side=tk.LEFT)

        self.telefoneEntry = tk.Entry(self.janela4, width=30, font=self.fontePadrao)
        self.telefoneEntry.pack(side=tk.LEFT)

        # Frame para o campo de E-mail
        self.janela5 = tk.Frame(self.janela)
        self.janela5.pack(pady=5)

        self.emailLabel = tk.Label(self.janela5, text="E-mail", font=self.fontePadrao)
        self.emailLabel.pack(side=tk.LEFT)

        self.emailEntry = tk.Entry(self.janela5, width=30, font=self.fontePadrao)
        self.emailEntry.pack(side=tk.LEFT)

        # Frame para o campo de Usuário
        self.janela6