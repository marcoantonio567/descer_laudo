import tkinter as tk
from tkinter import ttk, messagebox


class RespostaDinamica:
    def __init__(self, root, texto_pergunta, opcoes):
        self.root = root
        self.texto_pergunta = texto_pergunta
        self.opcoes = opcoes

        self.resposta_var = tk.StringVar()
        self.resposta_escolhida = None

        # Calcular altura da janela baseada na quantidade de opções
        altura_base = 200  # Altura base para título e botão
        altura_por_opcao = 40  # Altura para cada opção
        altura_total = altura_base + len(opcoes) * altura_por_opcao

        self.root.title("Pergunta")
        self.root.geometry(f"520x{altura_total}")
        self.root.configure(bg="#ebf5fe")

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
        titulo = ttk.Label(self.root, text=self.texto_pergunta,
                           font=("Segoe UI", 14, "bold"),
                           background="#ebf5fe",
                           foreground="#0d47a1")
        titulo.pack(pady=(30, 20))

        for opcao in self.opcoes:
            ttk.Radiobutton(self.root, text=opcao,
                            variable=self.resposta_var,
                            value=opcao).pack(anchor="center")

        botao_confirmar = ttk.Button(self.root, text="Confirmar", command=self.confirmar_escolha)
        botao_confirmar.pack(pady=30)

    def confirmar_escolha(self):
        resposta = self.resposta_var.get()
        if resposta:
            self.resposta_escolhida = resposta
            self.root.destroy()
        else:
            messagebox.showwarning("Atenção", "Por favor, selecione uma opção.")


def selecionar_resposta(texto_pergunta, opcoes):
    root = tk.Tk()
    app = RespostaDinamica(root, texto_pergunta, opcoes)
    root.mainloop()
    return app.resposta_escolhida
