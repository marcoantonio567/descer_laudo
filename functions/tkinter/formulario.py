import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry


class Formulario:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulário")
        self.root.geometry("500x550")
        self.root.configure(bg="#1e1e2f")

        self._estilizar()
        self._criar_interface()

    def _estilizar(self):
        style = ttk.Style(self.root)
        style.theme_use('clam')
        style.configure('TButton', font=('Segoe UI', 10), background='#007acc', foreground='white')
        style.configure('TLabel', font=('Segoe UI', 10), background='#1e1e2f', foreground='white')
        style.configure('TEntry', padding=5)
        style.configure('TCombobox', padding=5)

    def _criar_interface(self):
        container = tk.Frame(self.root, bg="#1e1e2f")
        container.pack(fill="both", expand=True)

        canvas = tk.Canvas(container, bg="#1e1e2f", highlightthickness=0)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)

        self.scrollable_frame = tk.Frame(canvas, bg="#1e1e2f")
        window = canvas.create_window((0, 0), window=self.scrollable_frame, anchor="n")

        def resize_canvas(event):
            canvas.itemconfig(window, width=event.width)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.bind("<Configure>", resize_canvas)

        canvas.bind_all(
            "<MouseWheel>",
            lambda event: canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        )

        self._construir_campos(self.scrollable_frame)

    def _construir_campos(self, frame):
        padding = {'padx': 20, 'pady': 5}

        ttk.Label(frame, text="Selecione a Agência Solicitante:").pack(**padding)
        self.campo2 = ttk.Entry(frame)
        self.campo2.pack(fill="x", **padding)

        ttk.Label(frame, text="Selecione o Fluid:").pack(**padding)
        self.campo3 = ttk.Entry(frame)
        self.campo3.pack(fill="x", **padding)

        ttk.Label(frame, text="Selecione a Data de solicitação:").pack(**padding)
        self.campo4 = DateEntry(
            frame,
            date_pattern='dd/mm/yyyy',
            background='#007acc',
            foreground='white',
            borderwidth=2
        )
        self.campo4.pack(fill="x", **padding)

        ttk.Label(frame, text="Selecione o Proponente:").pack(**padding)
        self.campo5 = ttk.Entry(frame)
        self.campo5.pack(fill="x", **padding)

        

        ttk.Label(frame, text="Nome e telefone de quem vai receber o vistoriador:").pack(**padding)
        self.campo8 = ttk.Entry(frame)
        self.campo8.pack(fill="x", **padding)

        self.botao_confirmar = ttk.Button(frame, text="Confirmar", command=self.coletar_dados)
        self.botao_confirmar.pack(pady=10)

    def coletar_dados(self):
        campos = {
            "Agência Solicitante": self.campo2.get().strip(),
            "Fluid": self.campo3.get().strip(),
            "Data": self.campo4.get().strip(),
            "Proponente": self.campo5.get().strip(),
            "Responsável pela visita": self.campo8.get().strip()
        }

        for chave, valor in campos.items():
            if valor == "":
                messagebox.showerror("Erro", f"O campo '{chave}' não pode ficar vazio.")
                return

        self.dados = campos
        self.root.destroy()


def dados_formulario():
    root = tk.Tk()
    formulario = Formulario(root)
    root.mainloop()

    return formulario.dados
