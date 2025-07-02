import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from functions.tkinter.input_zip import *
import os
import shutil
import rarfile
import zipfile
import glob


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
def mover_zip(destination_path, via_email='sim'):
    if via_email.strip().lower() == 'não':
        arquivo_selecionado = selecionar_arquivo_comprimido_obrigatorio()

        if not arquivo_selecionado or not os.path.isfile(arquivo_selecionado):
            print("Nenhum arquivo válido selecionado.")
            return None

        if not os.path.exists(destination_path):
            os.makedirs(destination_path)

        nome_arquivo = os.path.basename(arquivo_selecionado)
        destino = os.path.join(destination_path, nome_arquivo)

        try:
            shutil.move(arquivo_selecionado, destino)
            print(f"Arquivo {nome_arquivo} movido para {destination_path} com sucesso.")
            return destino
        except Exception as e:
            print(f"Erro ao mover o arquivo: {e}")
            return None

    else:
        downloads_path = os.path.expanduser("~/Downloads")

        if not os.path.exists(downloads_path):
            print(f"O diretório {downloads_path} não existe.")
            return None

        if not os.path.exists(destination_path):
            os.makedirs(destination_path)

        files = os.listdir(downloads_path)

        compressed_files = [f for f in files if f.endswith('.rar') or f.endswith('.zip')]

        if not compressed_files:
            print("Nenhum arquivo .rar ou .zip encontrado na pasta de downloads.")
            return None

        first_file = compressed_files[0]
        source_file = os.path.join(downloads_path, first_file)
        destination_file = os.path.join(destination_path, first_file)

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
