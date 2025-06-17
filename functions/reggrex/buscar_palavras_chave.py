import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from functions.tkinter.input_Texto_dinamico import input_texto_dinamico
from functions.tkinter.campo_dinamico_opcoes import selecionar_resposta
from functions.tkinter.data_dinamica import input_data_dinamico

import re

def extrair_nome(texto):
    # Usando expressão regular para encontrar o padrão "Nome: <nome>"
    padrao = r"Nome:\s*([A-Za-z\s]+)"
    correspondencia = re.search(padrao, texto)

    if correspondencia:
        nome = correspondencia.group(1).strip()  # Remove espaços extras
        nome = nome.replace(" Conta", "")  # Remove "Conta" se aparecer no final
        return nome
    else:
        return input_texto_dinamico("O nome não foi encontrado por favor digite o nome")
    
def encontrar_data(texto):
    # Expressão regular para capturar o formato "21 de jan de 2025"
    regex = r"\b(\d{1,2})\s+de\s+([a-z]{3})\s+de\s+(\d{4})\b"

    # Buscar a data no texto
    match = re.search(regex, texto)

    if match:
        # Capturar os grupos e reconstruir a data
        dia, mes, ano = match.groups()
        return f"{dia} de {mes} de {ano}"
    else:
        return input_data_dinamico()
    
def verificar_tipo_laudo(texto):
    # Expressão regular para pegar a primeira palavra após "Tipo de Imóvel:"
    padrao = r"Tipo de Imóvel:\s*(\w+)"

    # Procurando o padrão no texto
    resultado = re.search(padrao, texto)

    if resultado:
        tipo_imovel = resultado.group(1)
        tipo_imovel.lower() in ['rural', 'urbano']
        return tipo_imovel.capitalize()
    else:
        resposta = selecionar_resposta("deseja seguir esse laudo como maquinario?",["Sim", "Não"])
        if resposta == 'Sim':
            return None
        else:
            resposta = selecionar_resposta("Qual tipo de laudo",["Rural", "Urbano"])
            return resposta
def extrair_agencia_cnpj(texto):
     # Usando expressão regular para capturar tudo entre "Agência:" e "CNPJ"
    padrao = r'Agencia:\s*(.*?)\s*CNPJ'
    resultado = re.search(padrao, texto)
    
    if resultado:
        return resultado.group(1).strip()  # Retorna o texto encontrado entre as palavras
    else:
        return input_texto_dinamico("Agencia não foi encontrada por favor digite a Agencia")  # Caso não encontre o padrão
def extrair_quem_vai_Receber_vistoriador_rural_urbano(texto):
    # Usando expressão regular para capturar tudo entre "vistoriador Nome:" e "Telefone:"
    padrao = r'vistoriador Nome:\s*(.*?)\s*Telefone:'
    resultado = re.search(padrao, texto)
    
    if resultado:
        return resultado.group(1).strip()  # Retorna o texto encontrado entre as palavras
    else:
        return input_texto_dinamico("quem ira receber o vistoriador não foi encontrado\n por favor digite o nome")  # Caso não encontre o padrão
def extrair_telefone_numero_rural_urbano(texto):
    # Usando expressão regular para capturar tudo entre "Telefone:" e "Número"
    padrao = r'Telefone:\s*(.*?)\s*Número'
    resultado = re.search(padrao, texto)
    
    if resultado:
        return resultado.group(1).strip()  # Retorna o texto encontrado entre as palavras
    else:
        return input_texto_dinamico("O telefone não foi encontrado por favor digite o telefone")  # Caso não encontre o padrão
def extrair_telefone_vistoriador(texto):
    # Expressão regular para capturar tudo entre "Telefone:" e "Contato"
    padrao = r"Telefone:\s*(.*?)\s*(?=Contato)"
    
    # Encontrando todas as ocorrências
    resultado = re.search(padrao, texto, re.DOTALL)
    
    if resultado:
        return resultado.group(1).strip()  # Retorna o texto encontrado entre "Telefone:" e "Contato"
    else:
        return input_texto_dinamico("O telefone não foi encontrado por favor digite o telefone")
def pegar_nome_vistoriador(texto):
    # Expressão regular para encontrar a palavra "consorciado" seguida pelo texto entre "Nome:" e "Telefone:"
    padrao = r'consorciado.*?Nome:(.*?)Telefone:'
    
    # Buscar o primeiro padrão no texto
    resultado = re.search(padrao, texto, re.DOTALL)
    
    # Se encontrar, retorna o conteúdo entre "Nome:" e "Telefone:", senão retorna None
    if resultado:
        return resultado.group(1).strip()  # Retorna o conteúdo entre "Nome:" e "Telefone:"
    else:
        return input_texto_dinamico("O nome do consorciado não foi encontrado por favor digite o nome")
def extrair_numeros_fluid(texto):

    padrao = r'\b\d{7,8}\b'  # Procura por sequências de 7 ou 8 dígitos
    correspondencia = re.search(padrao, texto)
    if correspondencia:
        return correspondencia.group()
    else:
        return input_texto_dinamico("O fluid não foi encontrado por favor digite o fluid")