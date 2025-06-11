import re
import os
import email
from bs4 import BeautifulSoup
from email.policy import default
from pdf2image import convert_from_path



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

