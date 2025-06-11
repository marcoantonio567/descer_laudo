from functions.manipular_textos.textos import *
from functions.manipular_textos.manipular_textos import *
from functions.manipular_windos.manipular_windos import *
from functions.outras_funcoes.outras_funcoes import *
from functions.pyaytogui.funcoes_teclado_mouse import *
from functions.reggrex.buscar_palavras_chave import *
from functions.tkinter.escolher_city import *
from functions.tkinter.fazer_campos_dinamicos import *

caminho = encontrar_primeiro_eml()
texto = ler_arquivo_eml(caminho)
tipo_laudo = verificar_tipo_laudo(texto)
nome_proponente_geral = extrair_nome(texto)
data = encontrar_data(texto)
data_convertida = converter_data(data)
data_adcionada_7_dias = adicionar_7_dias(data_convertida)
agencia = extrair_agencia_cnpj(texto)
fluid = str(extrair_numeros_fluid(texto))
quem_vai_Receber_vistoriador = extrair_quem_vai_Receber_vistoriador_rural_urbano(texto)
telefone = extrair_telefone_numero_rural_urbano(texto)
telefone_vistoriador = extrair_telefone_vistoriador(texto)
nome_vistoriador = pegar_nome_vistoriador(texto)

if tipo_laudo == 'Rural':
    
    caminho_proponente_e_criacao_pasta = criar_pasta(caminho_rural,nome_modelo(fluid,nome_proponente_geral))
    criar_estutura_e_Retornar_documentos = criar_estrutura_de_pastas(caminho_proponente_e_criacao_pasta,estrutura_de_pastas_rural)
    caminho_zip_e_recortar_zip = mover_zip(criar_estutura_e_Retornar_documentos)
    extrair_arquivo_zip(caminho_zip_e_recortar_zip)#aqui ele vai extrair o arquivo zip na propria pasta
    pasta_documentos , pasta_png = obeter_pasta_documentos_e_png(caminho_proponente_e_criacao_pasta)
    convert_pdfs_to_png(pasta_documentos,pasta_png)
    cidade = escolher_cidade()

    root = tk.Tk() #criar a interface grafica para escolher as areas
    app = DynamicInputsApp(root) #para charmar os campos dinamicos e so colocar app.values
    root.mainloop()#fim da interface grafica para escolher as areas

    abrir_link(link)#abrir o link do google sheets
    janela_dinamica()#janela de espera para carregar a pagina do google sheets

    clicar_centro_tela()#clicar no centro da tela
    ir_pra_celula_A1()#ir para a celula A1
    ir_pra_ultima_celula_da_coluna()
    
    for area_matricula in app.values:
        time.sleep(0.3)
        escrever_texto('Sicredi')
        apertar_Tab()
        escrever_texto(agencia)
        apertar_Tab()
        escrever_texto(fluid)
        apertar_Tab()
        escrever_texto(data_convertida)#aqui ele vai escrever a data de solicitação
        apertar_Tab()
        escrever_texto(data_adcionada_7_dias)#aqui ele vai escrever a data de entrega
        apertar_Tab()
        escrever_texto("Rural")
        apertar_Tab()
        escrever_texto(nome_proponente_geral)
        apertar_Tab()
        escrever_texto(cidade)
        apertar_Tab()
        escrever_texto(area_matricula)
        escrever_texto(' ha')
        for i in range(3):
            apertar_Tab()
            
        escrever_texto(quem_vai_Receber_vistoriador)
        apertar_espaco()
        escrever_texto(telefone)
        apertar_Tab()
        apertar_home()
        time.sleep(0.5)
        
        apertar_pra_baixo()
    deletar_primeiro_eml()
    
elif tipo_laudo == 'Urbano':
    
    caminho_proponente_e_criacao_pasta = criar_pasta(caminho_urbano,nome_modelo(fluid,nome_proponente_geral))
    criar_estutura_e_Retornar_documentos = criar_estrutura_de_pastas(caminho_proponente_e_criacao_pasta,estrutura_de_pastas_urbano)
    caminho_zip_e_recortar_zip = mover_zip(criar_estutura_e_Retornar_documentos)
    extrair_arquivo_zip(caminho_zip_e_recortar_zip)#aqui ele vai extrair o arquivo zip na propria pasta
    pasta_documentos , pasta_png = obeter_pasta_documentos_e_png(caminho_proponente_e_criacao_pasta)
    convert_pdfs_to_png(pasta_documentos,pasta_png)
    cidade = escolher_cidade()
    
    root = tk.Tk() #criar a interface grafica para escolher as areas
    app = DynamicInputsApp(root) #para charmar os campos dinamicos e so colocar app.values
    root.mainloop()#fim da interface grafica para escolher as areas

    abrir_link(link)#abrir o link do google sheets
    janela_dinamica()#janela de espera para carregar a pagina do google sheets

    clicar_centro_tela()#clicar no centro da tela
    for area_matricula in app.values:
        time.sleep(0.3)
        ir_pra_celula_A1()#ir para a celula A1
        ir_pra_ultima_celula_da_coluna()
        
    
        escrever_texto('Sicredi')
        apertar_Tab()
        escrever_texto(agencia)
        apertar_Tab()
        escrever_texto(fluid)
        apertar_Tab()
        escrever_texto(data_convertida)#aqui ele vai escrever a data de solicitação
        apertar_Tab()
        escrever_texto(data_adcionada_7_dias)#aqui ele vai escrever a data de entrega
        apertar_Tab()
        escrever_texto("Rural")
        apertar_Tab()
        escrever_texto(nome_proponente_geral)
        apertar_Tab()
        escrever_texto(cidade)
        apertar_Tab()
        escrever_texto(area_matricula)
        escrever_texto(' m²')
        for i in range(3):
            apertar_Tab()
            
        escrever_texto(quem_vai_Receber_vistoriador)
        apertar_espaco()
        escrever_texto(telefone)
        
        apertar_Tab()
        apertar_home()
        time.sleep(0.5)
        apertar_pra_baixo()

    deletar_primeiro_eml()
    
elif tipo_laudo is None:
    
    caminho_proponente_e_criacao_pasta = criar_pasta(caminho_maquinario,nome_modelo(fluid,nome_proponente_geral))
    criar_estutura_e_Retornar_documentos = criar_estrutura_de_pastas(caminho_proponente_e_criacao_pasta,estrutura_de_pastas_maquinario)
    caminho_zip_e_recortar_zip = mover_zip(criar_estutura_e_Retornar_documentos)
    extrair_arquivo_zip(caminho_zip_e_recortar_zip)#aqui ele vai extrair o arquivo zip na propria pasta
    pasta_documentos , pasta_png = obeter_pasta_documentos_e_png(caminho_proponente_e_criacao_pasta)
    convert_pdfs_to_png(pasta_documentos,pasta_png)
    cidade = escolher_cidade()

    abrir_link(link)#abrir o link do google sheets
    janela_dinamica()#janela de espera para carregar a pagina do google sheets

    clicar_centro_tela()#clicar no centro da tela
    ir_pra_celula_A1()#ir para a celula A1
    ir_pra_ultima_celula_da_coluna()
    
    
    escrever_texto('Sicredi')
    apertar_Tab()
    escrever_texto(agencia)
    apertar_Tab()
    escrever_texto(fluid)
    apertar_Tab()
    escrever_texto(data_convertida)#aqui ele vai escrever a data de solicitação
    apertar_Tab()
    escrever_texto(data_adcionada_7_dias)#aqui ele vai escrever a data de entrega
    apertar_Tab()
    escrever_texto("Consórcio")
    apertar_Tab()
    escrever_texto(nome_proponente_geral)
    apertar_Tab()
    escrever_texto(cidade)
    
    for i in range(4):
        apertar_Tab()
        
    escrever_texto(nome_vistoriador)
    apertar_espaco()
    escrever_texto(telefone_vistoriador)
    
    apertar_Tab()
    apertar_home()
    time.sleep(0.5)
    apertar_pra_baixo()
    deletar_primeiro_eml()
    

janela_dinamica('terminou sugira melhorias')