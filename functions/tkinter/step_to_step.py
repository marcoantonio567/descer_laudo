import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Lista de passos (imagem + legenda)
passos = [
    {"imagem": "images/primeiro.png", "legenda": "se o email for via suite do sicredi siga os passos a seguir caso contratrio aperte em pular\n1. Abra o E-mail Desejado e abra suas Configurações"},
    {"imagem": "images/segundo.png", "legenda": "2. Clique em baixar mensagem e coloque em Downloads"},
    {"imagem": "images/terceiro.png", "legenda": "3. Arraste o E-mail para baixo e aperte em baixar\nagora leia com atentamente as janelas de interface"},
]

class PassoAPassoApp(tk.Tk):    
    def __init__(self):
        super().__init__()
        self.title("Tutorial Interativo")
        self.geometry("620x520")
        self.configure(bg="#f7f7f7")
        self.passo_atual = 0

        # Frame principal
        self.frame = ttk.Frame(self)
        self.frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Imagem
        self.label_imagem = tk.Label(self.frame)
        self.label_imagem.pack(pady=10)

        # Legenda
        self.label_legenda = tk.Label(self.frame, font=("Arial", 14), wraplength=550, bg="#f7f7f7")
        self.label_legenda.pack(pady=10)

        # Botões de navegação
        self.frame_botoes = tk.Frame(self.frame, bg="#f7f7f7")
        self.frame_botoes.pack(pady=20)

        self.botao_anterior = ttk.Button(self.frame_botoes, text="⟨ Anterior", command=self.voltar_passo)
        self.botao_anterior.grid(row=0, column=0, padx=5)

        self.botao_proximo = ttk.Button(self.frame_botoes, text="Próximo ⟩", command=self.avancar_passo)
        self.botao_proximo.grid(row=0, column=1, padx=5)

        self.botao_pular = ttk.Button(self.frame_botoes, text="Pular ⏭", command=self.pular_para_final)
        self.botao_pular.grid(row=0, column=2, padx=5)

        self.botao_entendi = ttk.Button(self.frame_botoes, text="Entendi ✅", command=self.finalizar)
        self.botao_entendi.grid(row=0, column=3, padx=5)
        self.botao_entendi.grid_remove()  # Esconde no início

        self.exibir_passo()

    def exibir_passo(self):
        passo = passos[self.passo_atual]
        imagem = Image.open(passo["imagem"]).resize((400, 300))
        self.tk_image = ImageTk.PhotoImage(imagem)

        self.label_imagem.configure(image=self.tk_image)
        self.label_legenda.configure(text=passo["legenda"])

        # Atualiza botões
        self.botao_anterior["state"] = "normal" if self.passo_atual > 0 else "disabled"

        if self.passo_atual == len(passos) - 1:
            self.botao_proximo.grid_remove()
            self.botao_pular.grid_remove()
            self.botao_entendi.grid()
        else:
            self.botao_proximo.grid()
            self.botao_pular.grid()
            self.botao_entendi.grid_remove()

    def avancar_passo(self):
        if self.passo_atual < len(passos) - 1:
            self.passo_atual += 1
            self.exibir_passo()

    def voltar_passo(self):
        if self.passo_atual > 0:
            self.passo_atual -= 1
            self.exibir_passo()

    def pular_para_final(self):
        self.passo_atual = len(passos) - 1
        self.exibir_passo()

    def finalizar(self):
        self.destroy()  # Fecha a janela

def passo_passo():
    app = PassoAPassoApp()
    app.mainloop()
