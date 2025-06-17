import tkinter as tk
from tkinter import filedialog, messagebox


def selecionar_arquivo_comprimido_obrigatorio():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal

    arquivo = None

    while not arquivo:
        arquivo = filedialog.askopenfilename(
            title="Selecione um arquivo ZIP ou RAR",
            filetypes=[
                ("Arquivos compactados", "*.zip *.rar"),
                ("Arquivo ZIP", "*.zip"),
                ("Arquivo RAR", "*.rar"),
                ("Todos os arquivos", "*.*")
            ]
        )

        if not arquivo:
            messagebox.showwarning("Aviso", "Você precisa selecionar um arquivo ZIP ou RAR!")

    print(f"Arquivo selecionado: {arquivo}")
    return arquivo


