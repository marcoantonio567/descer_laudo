import tkinter as tk

class DynamicInputsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Entrada Dinâmica")
        self.root.configure(bg='#2d2d2d')
        self.root.geometry("400x500")
        
        # Estilo geral
        self.fonte = ('Arial', 10)
        self.cor_principal = '#6c5ce7'
        self.cor_fundo = '#2d2d2d'
        self.cor_texto = '#ffffff'
        self.cor_input = '#404040'
        
        self.input_fields = []
        self.values = []
        
        self.root.bind('<Return>', self.handle_enter)
        self.create_widgets()
    
    def create_widgets(self):
        # Frame principal
        self.main_frame = tk.Frame(self.root, bg=self.cor_fundo)
        self.main_frame.pack(padx=20, pady=20, fill=tk.X)
        
        # Título
        tk.Label(self.main_frame, 
                text="Gerador de Campos Dinâmicos",
                font=('Arial', 12, 'bold'),
                bg=self.cor_fundo,
                fg=self.cor_principal).pack(pady=10)
        
        # Entrada para número de campos
        tk.Label(self.main_frame, 
                text="Quantidade de Matriculas:",
                font=self.fonte,
                bg=self.cor_fundo,
                fg=self.cor_texto).pack(anchor=tk.W)
        
        self.num_input = tk.Entry(self.main_frame,
                                font=self.fonte,
                                bg=self.cor_input,
                                fg=self.cor_texto,
                                insertbackground=self.cor_texto,
                                relief=tk.FLAT)
        self.num_input.pack(pady=5, fill=tk.X)
        
        # Botão de criação
        self.create_btn = tk.Button(self.main_frame,
                                  text="Criar Campos",
                                  command=self.create_inputs,
                                  bg=self.cor_principal,
                                  fg=self.cor_texto,
                                  activebackground='#5b4bc4',
                                  activeforeground=self.cor_texto,
                                  font=self.fonte,
                                  relief=tk.FLAT)
        self.create_btn.pack(pady=10, fill=tk.X)
        
        # Frame para inputs dinâmicos
        self.inputs_frame = tk.Frame(self.root, bg=self.cor_fundo)
        self.inputs_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
    
    def handle_enter(self, event):
        if self.submit_active:
            self.get_values()
            self.root.destroy()
        else:
            self.create_inputs()
    
    def create_inputs(self):
        # Limpar campos existentes
        for widget in self.inputs_frame.winfo_children():
            widget.destroy()
        self.input_fields.clear()
        
        try:
            num = int(self.num_input.get())
            if num <= 0:
                raise ValueError
        except ValueError:
            return
        
        # Criar novos campos
        for i in range(num):
            frame = tk.Frame(self.inputs_frame, bg=self.cor_fundo)
            frame.pack(pady=5, fill=tk.X)
            
            tk.Label(frame,
                    text=f"área {i+1}:",
                    font=self.fonte,
                    bg=self.cor_fundo,
                    fg=self.cor_texto).pack(side=tk.LEFT)
            
            entry = tk.Entry(frame,
                           font=self.fonte,
                           bg=self.cor_input,
                           fg=self.cor_texto,
                           insertbackground=self.cor_texto,
                           relief=tk.FLAT)
            entry.pack(side=tk.RIGHT, fill=tk.X, expand=True)
            self.input_fields.append(entry)
        
        self.submit_active = True
    
    def get_values(self):
        self.values = [entry.get() for entry in self.input_fields]
        


