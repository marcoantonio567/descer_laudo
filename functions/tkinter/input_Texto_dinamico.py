import tkinter as tk
from tkinter import ttk

def input_texto_dinamico(titulo):
    input_selecionado = None  # Variável para armazenar a input escolhida

    def confirmar(event=None):
        nonlocal input_selecionado
        input_text = entrada.get().strip()  # Remove espaços extras
        if input_text:
            input_selecionado = input_text
            root.destroy()

    # Criar a janela principal
    root = tk.Tk()
    root.title(titulo)
    root.geometry("400x200")
    root.configure(bg="#282c34")
    
    # Centralizar janela na tela
    root.eval('tk::PlaceWindow . center')

    # Estilização
    estilo = ttk.Style()
    estilo.configure("TLabel", foreground="white", background="#282c34", font=("Arial", 12))
    estilo.configure("TEntry", font=("Arial", 12), padding=5)
    estilo.configure("TButton", font=("Arial", 12), padding=5)

    # Frame container para melhor organização
    frame = ttk.Frame(root, padding=20)
    frame.pack(expand=True, fill=tk.BOTH)
    frame['style'] = 'Background.TFrame'
    estilo.configure('Background.TFrame', background='#282c34')

    # Rótulo
    label = ttk.Label(frame, text=f"Digite a {titulo.lower()}:")
    label.pack(pady=(0, 10))

    # Entrada
    entrada = ttk.Entry(frame, width=30)
    entrada.pack(pady=5)
    entrada.bind("<Return>", confirmar)

    # Botão de confirmação
    botao = ttk.Button(frame, text="Confirmar", command=confirmar)
    botao.pack(pady=(10, 0))

    # Focar no campo de entrada e garantir que a janela esteja no topo
    entrada.focus_force()
    root.attributes('-topmost', True)
    root.after_idle(root.attributes, '-topmost', False)

    # Tratar fechamento da janela
    root.protocol("WM_DELETE_WINDOW", root.destroy)

    root.mainloop()
    
    return input_selecionado