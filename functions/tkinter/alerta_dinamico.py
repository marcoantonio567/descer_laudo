import tkinter as tk

def show_alert_dinamic(message):
    def flash():
        # Alterna o fundo entre as duas cores
        nonlocal current_color_index
        current_color_index = 1 - current_color_index
        cor = colors[current_color_index]
        root.config(bg=cor)
        label.config(bg=cor)
        root.after(1000, flash)

    # Cores de alerta (ex.: amarelo e vermelho)
    colors = ["yellow", "red"]
    current_color_index = 0

    # Cria janela
    root = tk.Tk()
    root.title("!!! ALERTA !!!")
    root.attributes("-topmost", True)  # sempre na frente
    root.config(bg=colors[current_color_index])

    # Texto dinâmico
    label = tk.Label(
        root,
        text=message,
        font=("Helvetica", 18, "bold"),
        bg=colors[current_color_index],
        fg="black",
        justify="center",
        wraplength=600  # evita janelas absurdamente largas; ajuste se quiser
    )
    label.pack(padx=20, pady=(20, 10))

    # Botão de fechar
    button = tk.Button(
        root,
        text="Entendi",
        font=("Helvetica", 14, "bold"),
        command=root.destroy
    )
    button.pack(pady=(0, 20))

    # Redimensiona janela ao conteúdo
    root.update_idletasks()
    largura = label.winfo_reqwidth() + 40
    altura = label.winfo_reqheight() + button.winfo_reqheight() + 60
    root.geometry(f"{largura}x{altura}")

    # Inicia o piscar
    flash()
    root.mainloop()


    
