import tkinter as tk
from tkinter import ttk

def escolher_cidade():
    cidade_selecionada = None  # Variável para armazenar a cidade escolhida

    def confirmar(event=None):
        nonlocal cidade_selecionada  # Permite modificar a variável externa
        cidade = entrada.get()
        if cidade:
            cidade_selecionada = cidade  # Armazena o valor digitado
            root.destroy()  # Fecha a interface de forma segura

    # Criar a janela principal
    root = tk.Tk()
    root.title("Qual o nome da cidade do imóvel")
    root.geometry("400x200")
    root.configure(bg="#282c34")

    # Estilização
    estilo = ttk.Style()
    estilo.configure("TLabel", foreground="white", background="#282c34", font=("Arial", 12))
    estilo.configure("TEntry", font=("Arial", 12))
    estilo.configure("TButton", font=("Arial", 12))

    # Rótulo
    label = ttk.Label(root, text="Digite o nome da cidade:")
    label.pack(pady=20)

    # Entrada
    entrada = ttk.Entry(root, width=30)
    entrada.pack()
    entrada.bind("<Return>", confirmar)  # Ativar Enter

    # Botão de confirmação
    botao = ttk.Button(root, text="Confirmar", command=confirmar)
    botao.pack(pady=10)

    # Focar no campo de entrada
    entrada.focus_force()

    # Executar a interface gráfica
    root.mainloop()
    #root.destroy()  # Fecha a janela após o loop principal

    return cidade_selecionada  # Retorna a cidade digitada