import tkinter as tk
from tkinter import ttk
import json


class EstadoCidadeSelector(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Seleção de Estado e Cidade")
        self.geometry("500x520")
        self.configure(bg="#f5f5f5")
        self.resultado = None

        # Estilo
        self.style = ttk.Style(self)
        self.style.theme_use('clam')

        self.header_font = ("Segoe UI", 15, "bold")
        self.label_font = ("Segoe UI", 11)
        self.entry_font = ("Segoe UI", 10)
        self.accent = "#2196f3"

        self.style.configure("Header.TLabel", background="#f5f5f5", foreground=self.accent, font=self.header_font)
        self.style.configure("TLabel", background="#f5f5f5", font=self.label_font)
        self.style.configure("TEntry", font=self.entry_font, padding=6, relief="flat")
        self.style.configure("Accent.TButton", background=self.accent, foreground="white", font=self.entry_font, padding=6, relief="flat")
        self.style.map("Accent.TButton",
                        background=[('active', '#1976d2')],
                        relief=[('pressed', 'sunken'), ('!pressed', 'raised')])

        with open('estados-cidades.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.states = sorted(item['sigla'] for item in data)
        self.cities_by_state = {item['sigla']: item['cidades'] for item in data}
        self.selected_state = None

        header = ttk.Label(self, text="Selecione Estado e Cidade", style="Header.TLabel")
        header.pack(pady=(15, 10))

        container = ttk.Frame(self, padding=10)
        container.pack(fill='both', expand=True, padx=20)

        # Estado
        state_frame = ttk.Labelframe(container, text="Estado", padding=10)
        state_frame.pack(fill='x', pady=(0, 15))
        self.state_var = tk.StringVar()
        self.state_entry = ttk.Entry(state_frame, textvariable=self.state_var, style="TEntry")
        self.state_entry.pack(fill='x', pady=(0, 8))
        self.state_entry.bind("<KeyRelease>", lambda e: (self.update_state_list(), self.verificar_selecao()))

        self.state_listbox = tk.Listbox(state_frame, height=5, font=self.entry_font,
                                        bd=1, relief="flat", highlightbackground="#ddd",
                                        highlightthickness=1, selectbackground=self.accent, selectforeground="white")
        self.state_listbox.pack(fill='both', expand=True)
        self.state_listbox.bind("<<ListboxSelect>>", self.on_state_select)

        # Cidade
        city_frame = ttk.Labelframe(container, text="Cidade", padding=10)
        city_frame.pack(fill='x')
        self.city_var = tk.StringVar()
        self.city_entry = ttk.Entry(city_frame, textvariable=self.city_var, style="TEntry", state='disabled')
        self.city_entry.pack(fill='x', pady=(0, 8))
        self.city_entry.bind("<KeyRelease>", lambda e: (self.update_city_list(), self.verificar_selecao()))

        self.city_listbox = tk.Listbox(city_frame, height=5, font=self.entry_font,
                                        bd=1, relief="flat", highlightbackground="#ddd",
                                        highlightthickness=1, selectbackground=self.accent, selectforeground="white")
        self.city_listbox.pack(fill='both', expand=True)
        self.city_listbox.bind("<<ListboxSelect>>", self.on_city_select)

        # Botões
        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=15)

        self.confirm_btn = ttk.Button(btn_frame, text="Confirmar", style="Accent.TButton",
                                        command=self.confirm_selection, state='disabled')
        self.confirm_btn.pack(side='left', padx=10)

        

        self.update_state_list()

    def update_state_list(self, event=None):
        search = self.state_var.get().lower()
        self.state_listbox.delete(0, tk.END)
        for state in self.states:
            if search in state.lower():
                self.state_listbox.insert(tk.END, state)

    def on_state_select(self, event):
        sel = self.state_listbox.curselection()
        if sel:
            state = self.state_listbox.get(sel[0])
            self.state_var.set(state)
            self.selected_state = state
            self.city_entry.config(state='normal')
            self.city_var.set('')
            self.update_city_list()
        self.verificar_selecao()

    def update_city_list(self, event=None):
        if not self.selected_state:
            return
        search = self.city_var.get().lower()
        cities = self.cities_by_state.get(self.selected_state, [])
        self.city_listbox.delete(0, tk.END)
        for city in cities:
            if search in city.lower():
                self.city_listbox.insert(tk.END, city)

    def on_city_select(self, event):
        sel = self.city_listbox.curselection()
        if sel:
            city = self.city_listbox.get(sel[0])
            self.city_var.set(city)
        self.verificar_selecao()


    def verificar_selecao(self, event=None):
        estado_ok = bool(self.state_var.get().strip())
        cidade_ok = bool(self.city_var.get().strip())
        if estado_ok and cidade_ok:
            self.confirm_btn.config(state='normal')
        else:
            self.confirm_btn.config(state='disabled')

    def confirm_selection(self):
        if self.selected_state and self.city_var.get():
            self.resultado = f'{self.city_var.get()} - {self.selected_state}'
        else:
            self.resultado = None
        self.destroy()


def selecionar_estado_cidade():
    app = EstadoCidadeSelector()
    app.mainloop()
    return app.resultado
