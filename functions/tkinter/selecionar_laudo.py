import tkinter as tk
from tkinter import ttk, messagebox

class BancoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Seleção de Instituição Financeira")
        self.root.geometry("520x360")
        self.root.configure(bg="#ebf5fe")  # azul claro

        self.banco_var = tk.StringVar()
        self.banco_escolhido = None  # Variável para armazenar o valor selecionado

        self._estilizar()
        self._construir_interface()

    def _estilizar(self):
        style = ttk.Style(self.root)
        style.theme_use("clam")
        style.configure("TRadiobutton",
                        font=("Segoe UI", 12),
                        background="#ebf5fe",
                        foreground="#1a237e",
                        padding=10)
        style.configure("TButton",
                        font=("Segoe UI", 12, "bold"),
                        background="#2196F3",
                        foreground="white")
        style.map("TButton",
                  background=[("active", "#1976D2")])

    def _construir_interface(self):
        titulo = ttk.Label(self.root, text="Selecione o banco desejado:",
                           font=("Segoe UI", 14, "bold"), background="#ebf5fe", foreground="#0d47a1")
        titulo.pack(pady=(30, 20))

        opcoes = ["Sicredi", "Sicoob", "BASA", "Particular"]
        for opcao in opcoes:
            ttk.Radiobutton(self.root, text=opcao, variable=self.banco_var, value=opcao).pack(anchor="center")

        botao_confirmar = ttk.Button(self.root, text="Confirmar", command=self.confirmar_escolha)
        botao_confirmar.pack(pady=30)

    def confirmar_escolha(self):
        banco_selecionado = self.banco_var.get()
        if banco_selecionado:
            self.banco_escolhido = banco_selecionado  # Armazena a escolha
            messagebox.showinfo("Banco Selecionado", f"Você selecionou: {banco_selecionado}")
            self.root.destroy()  # Fecha a janela após confirmação
        else:
            messagebox.showwarning("Nenhuma opção", "Por favor, selecione uma instituição.")

def selecionar_banco():
    root = tk.Tk()
    app = BancoApp(root)
    root.mainloop()
    return app.banco_escolhido  # Retorna o valor selecionado

