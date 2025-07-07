import tkinter as tk
from tkinter import messagebox, ttk

class GeradorDeInputs:
    def __init__(self, root, texto):
        self.root = root
        self.root.geometry("420x480")
        self._centralizar_janela()
        self.root.configure(bg='#1e1e2f')
        self.texto = texto
        self.root.title(self.tratar_tittle_dinamico())
        self.entradas = []
        self.valores = []  # <- Armazena os valores aqui
        self._estilizar()
        self._construir_interface()

    def _centralizar_janela(self):
        # Atualiza a janela para calcular suas dimensões
        self.root.update_idletasks()
        
        # Obtém as dimensões da tela
        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()
        
        # Obtém as dimensões da janela
        largura_janela = self.root.winfo_width()
        altura_janela = self.root.winfo_height()
        
        # Calcula a posição central
        pos_x = (largura_tela - largura_janela) // 2
        pos_y = (altura_tela - altura_janela) // 2
        
        # Define a posição da janela
        self.root.geometry(f'+{pos_x}+{pos_y}')

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

        # Criação do frame principal que conterá o canvas e a scrollbar
        self.frame_principal = tk.Frame(self.root, bg='#262637')
        self.frame_principal.pack(fill='both', expand=True)

        # Criação do canvas
        self.canvas = tk.Canvas(self.frame_principal, bg='#262637', highlightthickness=0)
        self.canvas.pack(side='left', fill='both', expand=True)

        # Adição da scrollbar
        self.scrollbar = ttk.Scrollbar(self.frame_principal, orient='vertical', command=self.canvas.yview)
        self.scrollbar.pack(side='right', fill='y')

        # Configuração do canvas
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox('all')))
        
        # Configuração do scroll com botão do meio do mouse
        self.canvas.bind("<MouseWheel>", self._on_mousewheel)
        self.canvas.bind("<Button-2>", self._start_scroll)  # Botão do meio (Button-2)
        self.canvas.bind("<B2-Motion>", self._on_scroll)
        self.canvas.bind("<ButtonRelease-2>", self._stop_scroll)

        # Criação do frame que conterá os inputs dentro do canvas
        self.frame_inputs = tk.Frame(self.canvas, bg='#262637', padx=20, pady=20)
        self.canvas.create_window((0, 0), window=self.frame_inputs, anchor='nw')

        self.btn_resultado = ttk.Button(self.root, text="Enviar", command=self.obter_valores)
        self.btn_resultado.pack(pady=10)
        self.btn_resultado.bind('<Return>', self.obter_valores)

    def _on_mousewheel(self, event):
        # Scroll com roda do mouse
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def _start_scroll(self, event):
        # Inicia o scroll com botão do meio
        self.canvas.scan_mark(event.x, event.y)

    def _on_scroll(self, event):
        # Movimento do scroll com botão do meio
        self.canvas.scan_dragto(event.x, event.y, gain=1)

    def _stop_scroll(self, event):
        # Para o scroll (opcional)
        pass

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

        # Atualiza a região de scroll após adicionar os widgets
        self.frame_inputs.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def obter_valores(self, event=None):
        self.valores = [entrada.get() for entrada in self.entradas]
        self.root.quit()     # Encerra o loop
        self.root.destroy()  # Destroi a janela

    def tratar_tittle_dinamico(self):
        if self.texto == 'Maquina':
            return f"Gerador de Maquinarios Dinâmicos"
        elif self.texto == 'Area':
            return f"Gerador de Matriculas Dinâmicos"

    def tratar_nome(self, with_s:bool):
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
    
    def tratar_nome_dinamico(self, valor):
        if self.texto == 'Maquina':
            return f"Nome do maquinario {valor}:"
        elif self.texto == 'Area':
            return f"Tamanho da area\nda matricula {valor}:"

def selecionar_matriculas_maquinas(text):
    root = tk.Tk()
    app = GeradorDeInputs(root, text)
    root.mainloop()
    return app.valores