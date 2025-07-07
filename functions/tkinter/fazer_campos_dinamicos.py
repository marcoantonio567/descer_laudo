import tkinter as tk
from tkinter import messagebox, ttk

class GeradorDeInputs:
    def __init__(self, root , texto):
        self.root = root
        self.root.geometry("420x480")
        self.root.configure(bg='#1e1e2f')
        self.texto = texto
        self.root.title(self.tratar_tittle_dinamico())
        self.entradas = []
        self.valores = []  # <- Armazena os valores aqui
        self._estilizar()
        self._construir_interface()

    def _estilizar(self):
        style = ttk.Style(self.root)
        style.theme_use('clam')
        style.configure('TButton', font=('Segoe UI', 10), padding=6, background='#2a72b5', foreground='white')
        style.map('TButton', background=[('active', '#1c4d7a')])
        style.configure('TLabel', font=('Segoe UI', 10), background='#1e1e2f', foreground='white')
        style.configure('TEntry', padding=5)

    def _construir_interface(self):
        self.frame_top = tk.Frame(self.root, bg='#2a2a3d', padx=20, pady=20)
        self.frame_top.pack(fill='x')

        self.label_qtd = ttk.Label(self.frame_top, text=f"Qual a quantidade de {self.tratar_nome(with_s=True)}\na avaliação vai ter? (1-10):")
        self.label_qtd.pack(side='left', padx=(0, 10))

        self.entry_qtd = ttk.Entry(self.frame_top, width=5)
        self.entry_qtd.pack(side='left')
        self.entry_qtd.bind('<Return>', self.criar_inputs)

        self.btn_gerar = ttk.Button(self.frame_top, text=f"Gerar {self.texto}s", command=self.criar_inputs)
        self.btn_gerar.pack(side='left', padx=10)

        self.frame_inputs = tk.Frame(self.root, bg='#262637', padx=20, pady=20)
        self.frame_inputs.pack(fill='both', expand=True)

        self.btn_resultado = ttk.Button(self.root, text="Enviar", command=self.obter_valores)
        self.btn_resultado.pack(pady=10)
        self.btn_resultado.bind('<Return>', self.obter_valores)

    def criar_inputs(self, event=None):
        try:
            qtd = int(self.entry_qtd.get())
            if qtd < 1 or qtd > 10:
                raise ValueError("Digite um número entre 1 e 10")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))
            return

        for widget in self.frame_inputs.winfo_children():
            widget.destroy()
        self.entradas.clear()

        for i in range(qtd):
            label = ttk.Label(self.frame_inputs, text=self.tratar_nome_dinamico(i+1), style='TLabel')
            label.grid(row=i, column=0, padx=5, pady=5, sticky='e')

            entrada = ttk.Entry(self.frame_inputs, width=30)
            entrada.grid(row=i, column=1, padx=5, pady=5)
            entrada.bind('<Return>', self.obter_valores)
            self.entradas.append(entrada)

        if self.entradas:
            self.entradas[0].focus()

    def obter_valores(self, event=None):
        self.valores = [entrada.get() for entrada in self.entradas]
        self.root.quit()     # Encerra o loop
        self.root.destroy()  # Destroi a janela

    def tratar_tittle_dinamico(self):
        if self.texto == 'Maquina':
            return f"Gerador de Maquinarios Dinâmicos"
        elif self.texto == 'Area':
            return f"Gerador de Matriculas Dinâmicos"

    def tratar_nome(self,with_s:bool):
        if self.texto == 'Maquina':
            if with_s == True:
                return 'Maquinas'
            elif with_s == False:
                return 'Maquina'
        elif self.texto == 'Area':
            if with_s == True:
                return 'Matriculas'
            elif with_s == False:
                return 'Matricula'
    
    def tratar_nome_dinamico(self,valor):
        if self.texto == 'Maquina':
            return f"Nome do maquinario {valor}:"
        elif self.texto == 'Area':
            return f"Tamanho da Matricula {valor}:"

def selecionar_matriculas_maquinas(text):
    root = tk.Tk()
    app = GeradorDeInputs(root,text)
    root.mainloop()
    return app.valores
