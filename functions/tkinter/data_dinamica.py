import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry


def input_data_dinamico(titulo):
    data_selecionada = None  # Variável para armazenar a data escolhida

    def confirmar(event=None):
        nonlocal data_selecionada  # Permite modificar a variável externa
        data = calendario.get()
        if data:
            data_selecionada = data  # Armazena a data selecionada
            root.destroy()  # Fecha a interface de forma segura

    # Criar a janela principal
    root = tk.Tk()
    root.title(titulo)
    root.geometry("400x250")
    root.configure(bg="#282c34")

    # Estilização
    estilo = ttk.Style()
    estilo.theme_use('clam')
    estilo.configure("TLabel", foreground="white", background="#282c34", font=("Arial", 12))
    estilo.configure("TButton", font=("Arial", 12, "bold"), background="#61afef", foreground="black")
    estilo.map("TButton", background=[("active", "#528bbd")])

    # Rótulo
    label = ttk.Label(root, text=titulo)
    label.pack(pady=20)

    # Calendário
    calendario = DateEntry(root, width=18, background="#61afef", foreground="black",
                           borderwidth=2, font=("Arial", 12), date_pattern='dd/mm/yyyy')
    calendario.pack()

    calendario.bind("<Return>", confirmar)  # Ativar Enter

    # Botão de confirmação
    botao = ttk.Button(root, text="Confirmar", command=confirmar)
    botao.pack(pady=15)

    # Focar no calendário
    calendario.focus_force()

    # Executar a interface gráfica
    root.mainloop()

    return data_selecionada  # Retorna a data escolhida


