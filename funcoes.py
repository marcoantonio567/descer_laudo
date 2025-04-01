import re
import os
import glob
import email
import shutil
import rarfile
import zipfile
import tkinter as tk
from tkinter import ttk
from bs4 import BeautifulSoup
from email.policy import default
from pdf2image import convert_from_path
from datetime import datetime , timedelta

def encontrar_primeiro_eml():
    # Caminho da pasta Downloads do usuário
    pasta_downloads = os.path.join(os.path.expanduser("~"), "Downloads")
    
    # Lista todos os arquivos na pasta Downloads
    arquivos = sorted(os.listdir(pasta_downloads))
    
    # Filtra os arquivos com extensão .eml
    arquivos_eml = [arquivo for arquivo in arquivos if arquivo.lower().endswith(".eml")]
    
    # Retorna o caminho completo do primeiro arquivo .eml encontrado, se houver
    if arquivos_eml:
        return os.path.join(pasta_downloads, arquivos_eml[0])
    else:
        return "Nenhum arquivo .eml encontrado."
def ler_arquivo_eml(caminho_arquivo):
    try:
        # Abrir e ler o conteúdo do arquivo EML
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()

        # Parse do conteúdo para um objeto de mensagem
        mensagem = email.message_from_string(conteudo, policy=default)

        # Decodificar o conteúdo da mensagem
        partes = []
        if mensagem.is_multipart():
            for parte in mensagem.walk():
                if parte.get_content_type() == 'text/plain':
                    partes.append(parte.get_payload(decode=True).decode(parte.get_content_charset()))
                elif parte.get_content_type() == 'text/html':
                    html_content = parte.get_payload(decode=True).decode(parte.get_content_charset())
                    # Remover tags HTML
                    texto_limpo = BeautifulSoup(html_content, 'html.parser').get_text()
                    partes.append(texto_limpo)
        else:
            if mensagem.get_content_type() == 'text/html':
                html_content = mensagem.get_payload(decode=True).decode(mensagem.get_content_charset())
                texto_limpo = BeautifulSoup(html_content, 'html.parser').get_text()
                partes.append(texto_limpo)
            else:
                partes.append(mensagem.get_payload(decode=True).decode(mensagem.get_content_charset()))

        # Unir as partes decodificadas
        mensagem_decodificada = "\n".join(partes)

        # Remover quebras de linha excessivas
        mensagem_sem_quebras = re.sub(r'(\n\s*)+', ' ', mensagem_decodificada).strip()

        # Retornar a mensagem completa e decodificada
        return mensagem_sem_quebras

    except Exception as e:
        print(f"Erro ao ler o arquivo EML: {e}")
        return None   
def extrair_nome(texto):
    # Usando expressão regular para encontrar o padrão "Nome: <nome>"
    padrao = r"Nome:\s*([A-Za-z\s]+)"
    correspondencia = re.search(padrao, texto)

    if correspondencia:
        nome = correspondencia.group(1).strip()  # Remove espaços extras
        nome = nome.replace(" Conta", "")  # Remove "Conta" se aparecer no final
        return nome
    else:
        return "Nome não encontrado."
def encontrar_data(texto):
    # Expressão regular para capturar o formato "21 de jan de 2025"
    regex = r"\b(\d{1,2})\s+de\s+([a-z]{3})\s+de\s+(\d{4})\b"

    # Buscar a data no texto
    match = re.search(regex, texto)

    if match:
        # Capturar os grupos e reconstruir a data
        dia, mes, ano = match.groups()
        return f"{dia} de {mes} de {ano}"

    return None
def verificar_tipo_laudo(texto):
    # Expressão regular para pegar a primeira palavra após "Tipo de Imóvel:"
    padrao = r"Tipo de Imóvel:\s*(\w+)"

    # Procurando o padrão no texto
    resultado = re.search(padrao, texto)

    if resultado:
        tipo_imovel = resultado.group(1)
        if tipo_imovel.lower() in ['rural', 'urbano']:
            return tipo_imovel.capitalize()
        else:
            return None
    else:
        return None
def extrair_agencia_cnpj(texto):
     # Usando expressão regular para capturar tudo entre "Agência:" e "CNPJ"
    padrao = r'Agencia:\s*(.*?)\s*CNPJ'
    resultado = re.search(padrao, texto)
    
    if resultado:
        return resultado.group(1).strip()  # Retorna o texto encontrado entre as palavras
    else:
        return None  # Caso não encontre o padrão
def extrair_quem_vai_Receber_vistoriador_rural_urbano(texto):
    # Usando expressão regular para capturar tudo entre "vistoriador Nome:" e "Telefone:"
    padrao = r'vistoriador Nome:\s*(.*?)\s*Telefone:'
    resultado = re.search(padrao, texto)
    
    if resultado:
        return resultado.group(1).strip()  # Retorna o texto encontrado entre as palavras
    else:
        return None  # Caso não encontre o padrão
def extrair_telefone_numero_rural_urbano(texto):
    # Usando expressão regular para capturar tudo entre "Telefone:" e "Número"
    padrao = r'Telefone:\s*(.*?)\s*Número'
    resultado = re.search(padrao, texto)
    
    if resultado:
        return resultado.group(1).strip()  # Retorna o texto encontrado entre as palavras
    else:
        return None  # Caso não encontre o padrão
def extrair_telefone_vistoriador(texto):
    # Expressão regular para capturar tudo entre "Telefone:" e "Contato"
    padrao = r"Telefone:\s*(.*?)\s*(?=Contato)"
    
    # Encontrando todas as ocorrências
    resultado = re.search(padrao, texto, re.DOTALL)
    
    if resultado:
        return resultado.group(1).strip()  # Retorna o texto encontrado entre "Telefone:" e "Contato"
    else:
        return None
def pegar_nome_vistoriador(texto):
    # Expressão regular para encontrar a palavra "consorciado" seguida pelo texto entre "Nome:" e "Telefone:"
    padrao = r'consorciado.*?Nome:(.*?)Telefone:'
    
    # Buscar o primeiro padrão no texto
    resultado = re.search(padrao, texto, re.DOTALL)
    
    # Se encontrar, retorna o conteúdo entre "Nome:" e "Telefone:", senão retorna None
    if resultado:
        return resultado.group(1).strip()  # Retorna o conteúdo entre "Nome:" e "Telefone:"
    else:
        return None
def extrair_numeros_fluid(texto):

    padrao = r'\b\d{7,8}\b'  # Procura por sequências de 7 ou 8 dígitos
    correspondencia = re.search(padrao, texto)
    if correspondencia:
        return correspondencia.group()
    else:
        return None
def criar_pasta(caminho, nome_da_pasta):
    try:
        # Cria o caminho completo da pasta
        caminho_completo = os.path.join(caminho, nome_da_pasta)
        
        # Verifica se a pasta já existe
        if not os.path.exists(caminho_completo):
            # Cria a pasta
            os.makedirs(caminho_completo)
            print(f"Pasta '{nome_da_pasta}' criada em '{caminho}' com sucesso!")
        else:
            print(f"A pasta '{nome_da_pasta}' já existe no caminho '{caminho}'.")
        
        # Retorna o caminho completo da pasta
        return caminho_completo
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        return None
def criar_estrutura_de_pastas(diretorio_base, estrutura_pastas):
    caminho_documentos = None

    for item in estrutura_pastas:
        if isinstance(item, tuple):
            # Se for uma tupla, o primeiro elemento é a pasta principal
            pasta_principal = os.path.join(diretorio_base, item[0])
            os.makedirs(pasta_principal, exist_ok=True)

            if item[0] == 'DOCUMENTOS':
                caminho_documentos = pasta_principal

            # O segundo elemento é a subpasta
            subpasta = os.path.join(pasta_principal, item[1])
            os.makedirs(subpasta, exist_ok=True)
        else:
            # Se for uma string, é uma pasta simples
            pasta = os.path.join(diretorio_base, item)
            os.makedirs(pasta, exist_ok=True)

            if item == 'DOCUMENTOS':
                caminho_documentos = pasta

    return caminho_documentos
def mover_zip(destination_path):
    downloads_path = os.path.expanduser("~/Downloads")
    # Certifique-se de que os diretórios existem
    if not os.path.exists(downloads_path):
        print(f"O diretório {downloads_path} não existe.")
        return None

    if not os.path.exists(destination_path):
        os.makedirs(destination_path)

    # Obtenha uma lista de arquivos na pasta de downloads
    files = os.listdir(downloads_path)

    # Filtre os arquivos com extensões .rar ou .zip
    compressed_files = [f for f in files if f.endswith('.rar') or f.endswith('.zip')]

    if not compressed_files:
        print("Nenhum arquivo .rar ou .zip encontrado na pasta de downloads.")
        return None

    # Pegue o primeiro arquivo encontrado
    first_file = compressed_files[0]
    source_file = os.path.join(downloads_path, first_file)
    destination_file = os.path.join(destination_path, first_file)

    # Mova o arquivo para o destino
    try:
        shutil.move(source_file, destination_file)
        print(f"Arquivo {first_file} movido para {destination_path} com sucesso.")
        return destination_file
    except Exception as e:
        print(f"Erro ao mover o arquivo: {e}")
        return None
def extrair_arquivo_zip(file_path):
    # Obtém o diretório onde o arquivo está localizado
    extract_to = os.path.dirname(file_path)

    # Verifica se o arquivo é um .zip
    if file_path.endswith('.zip'):
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        print(f"Arquivo .zip extraído em: {extract_to}")

    # Verifica se o arquivo é um .rar
    elif file_path.endswith('.rar'):
        try:
            with rarfile.RarFile(file_path, 'r') as rar_ref:
                rar_ref.extractall(extract_to)
            print(f"Arquivo .rar extraído em: {extract_to}")
        except rarfile.NeedFirstVolume:
            print("Erro: Este arquivo RAR faz parte de um volume dividido e precisa do primeiro volume.")
        except Exception as e:
            print(f"Erro ao extrair arquivo .rar: {e}")

    else:
        print("Formato de arquivo não suportado. Use .zip ou .rar.")   
def obeter_pasta_documentos_e_png(caminho_base):

    caminho_documentos = os.path.join(caminho_base, "DOCUMENTOS")
    caminho_png = os.path.join(caminho_documentos, "PNG")
    
    return caminho_documentos, caminho_png
def convert_pdfs_to_png(input_folder, output_folder): #função para converter pdfs em png
    poppler_path = "Release-24.08.0-0/poppler-24.08.0/Library/bin"
    if not os.path.exists(input_folder):
        print(f"Erro: A pasta de entrada '{input_folder}' não existe.")
        return

    os.makedirs(output_folder, exist_ok=True)
    
    pdf_files = [f for f in os.listdir(input_folder) if f.lower().endswith(".pdf")]
    
    if not pdf_files:
        print("Nenhum arquivo PDF encontrado na pasta de entrada.")
        return

    for filename in pdf_files:
        pdf_path = os.path.join(input_folder, filename)
        pdf_name = os.path.splitext(filename)[0]
        output_subfolder = os.path.join(output_folder, pdf_name)
        
        os.makedirs(output_subfolder, exist_ok=True)
        
        try:
            images = convert_from_path(pdf_path, poppler_path=poppler_path)
            for i, image in enumerate(images):
                image_path = os.path.join(output_subfolder, f"page_{i + 1}.png")
                image.save(image_path, "PNG")
                print(f"Página {i + 1} de '{filename}' salva em '{image_path}'")
        except Exception as e:
            print(f"Erro ao converter '{filename}': {e}")

    print("Conversão concluída!")
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
def converter_data(data_str):
    meses = {
        "jan": "01", "fev": "02", "mar": "03", "abr": "04",
        "mai": "05", "jun": "06", "jul": "07", "ago": "08",
        "set": "09", "out": "10", "nov": "11", "dez": "12"
    }
    
    partes = data_str.lower().split(" de ")
    dia = partes[0].zfill(2)
    mes = meses.get(partes[1], "00")
    ano = partes[2]
    
    return f"{dia}/{mes}/{ano}"
def adicionar_7_dias(data_str):
    # Converte a string para um objeto datetime
    data = datetime.strptime(data_str, "%d/%m/%Y")
    
    # Adiciona 7 dias
    nova_data = data + timedelta(days=7)
    
    # Retorna a nova data formatada
    return nova_data.strftime("%d/%m/%Y")
def deletar_primeiro_eml():
    # Obtém o diretório de Downloads do usuário
    downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")

    # Lista todos os arquivos .eml na pasta de Downloads
    eml_files = sorted(glob.glob(os.path.join(downloads_dir, "*.eml")))

    # Verifica se há arquivos .eml e deleta o primeiro encontrado
    if eml_files:
        first_eml = eml_files[0]
        try:
            os.remove(first_eml)
            print(f"Arquivo deletado: {first_eml}")
        except Exception as e:
            print(f"Erro ao deletar {first_eml}: {e}")
    else:
        print("Nenhum arquivo .eml encontrado na pasta de Downloads.")


