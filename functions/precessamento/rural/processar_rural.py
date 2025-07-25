import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


from functions.manipular_textos.textos import *
from functions.manipular_textos.manipular_textos import *
from functions.manipular_windos.manipular_windos import *
from functions.outras_funcoes.outras_funcoes import *
from functions.pyaytogui.funcoes_teclado_mouse import *
from functions.pyaytogui.google_sheets_atalhos import *
from functions.pyaytogui.mesclar_alinhar_celulas import *
from functions.pyaytogui.verificar_inserir_linhas import *
from functions.pyaytogui.converter_coordenadas import *
from functions.reggrex.buscar_palavras_chave import *
from functions.tkinter.input_Texto_dinamico import *
from functions.tkinter.input_de_cidade import *
from functions.tkinter.fazer_campos_dinamicos import *
from functions.tkinter.campo_dinamico_opcoes import *
from functions.tkinter.formulario import *
from functions.tkinter.input_zip import *
from functions.tkinter.alerta_dinamico import *




def gerenciar_rurais(instituicao):

    cordenadas_do_usuario = obter_resolucao_pyautogui()
    if instituicao == 'Sicredi':
        possui_eml = selecionar_resposta("possui um arquivo eml:",['Sim','não'])
    else:
        possui_eml = 'não'
        
    possui_documentos_via_email = possui_documentos_via_email = selecionar_resposta("Os Documentos Vinheram via E-mail?",['Sim','Não'])
    if possui_documentos_via_email == 'Não':
        possui_documentos = selecionar_resposta("possui algum tipo de documento?",['Sim','Não'])

        
    if possui_eml == 'Sim':
        caminho = encontrar_primeiro_eml()
        texto = ler_arquivo_eml(caminho)
        nome_proponente_geral = extrair_nome(texto)
        data = encontrar_data(texto)
        data_convertida = converter_data(data)
        data_adcionada_7_dias = adicionar_7_dias(data_convertida)
        agencia = extrair_agencia_cnpj(texto)
        fluid = str(extrair_numeros_fluid(texto))
        quem_vai_Receber_vistoriador = extrair_quem_vai_Receber_vistoriador_rural_urbano(texto)
        telefone = extrair_telefone_numero_rural_urbano(texto)
        cidade = selecionar_estado_cidade()

    else:
        dados = dados_formulario()
        cidade = selecionar_estado_cidade()
        nome_proponente_geral = dados['Proponente']
        data = dados['Data']
        data_convertida = converter_data(data)
        data_adcionada_7_dias = adicionar_7_dias(data_convertida)
        agencia = dados['Agência Solicitante']
        fluid = dados['Fluid']
        quem_vai_Receber_vistoriador = dados['Responsável pela visita']
        
    areas_matriculas =  selecionar_matriculas_maquinas('Area')    
    
    # Mapeamento das instituições para os caminhos
    caminhos = {
        'Sicredi': caminho_rural,
        'Banco da Amazônia': caminho_basa,
        'BASA': caminho_basa,
        'Particular': caminho_particular,
        'BRB': caminho_BRB,
        'Sicoob TO': caminho_sicoob,
        'Sicoob Uni': caminho_sicoob,
        'Caixa': caminho_caixa,
        'Pericia': caminho_pericia
    }

    # Verifica se a instituição está no dicionário
    if instituicao in caminhos:
        caminho_proponente_e_criacao_pasta = criar_pasta(
            caminhos[instituicao],
            nome_modelo(fluid, nome_proponente_geral)
        )


    criar_estutura_e_Retornar_documentos = criar_estrutura_de_pastas(caminho_proponente_e_criacao_pasta,estrutura_de_pastas_rural)
    if possui_documentos == 'Sim':
        if possui_eml == 'Sim' or possui_documentos_via_email == 'Sim':
            caminho_zip_e_recortar_zip = mover_zip(criar_estutura_e_Retornar_documentos,via_email=possui_documentos_via_email)
            extrair_arquivo_zip(caminho_zip_e_recortar_zip)#aqui ele vai extrair o arquivo zip na propria pasta
            pasta_documentos , pasta_png = obeter_pasta_documentos_e_png(caminho_proponente_e_criacao_pasta)
            convert_pdfs_to_png(pasta_documentos,pasta_png)
        
    



    quantidade_matriculas = len(areas_matriculas)
    abrir_link(link)#abrir o link do google sheets
    texto = texto = "ATENÇÃO!\n\n   Apos o voce apertar 'Entendi'\nnão mexa no computador\nenquanto não aparecer uma outra janela"
    show_alert_dinamic(texto)
    clicar_centro_tela()#clicar no centro da tela
    verificar_espaco_linha(quantidade_matriculas) #verificando e inserindo celulas no final da planilha , ele ja deixa na celula A1
    ir_pra_ultima_celula_da_coluna()
    visao_debaixo()
    if quantidade_matriculas==1:
        time.sleep(0.3)
        escrever_texto(str(instituicao))
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
        escrever_texto(areas_matriculas[0])#aqui digitando a area de matricula
        escrever_texto(' ha')
        for i in range(6):#indo pra quem ira receber o vistoriador
            apertar_Tab()
        if possui_eml == 'Sim':    
            escrever_texto(quem_vai_Receber_vistoriador)
            apertar_espaco()
            escrever_texto(telefone)
        else: 
            escrever_texto(quem_vai_Receber_vistoriador)
        apertar_Tab()
        apertar_home()
    if quantidade_matriculas>1:
        time.sleep(0.3)
        escrever_texto(str(instituicao))
        voltar_celula()
        mesclar_e_centralizar_celulas(quantidade_matriculas,cordenadas_do_usuario)
        
        apertar_Tab()
        escrever_texto(agencia)
        voltar_celula()
        mesclar_e_centralizar_celulas(quantidade_matriculas,cordenadas_do_usuario)
        
        apertar_Tab()
        escrever_texto(fluid)
        voltar_celula()
        mesclar_e_centralizar_celulas(quantidade_matriculas,cordenadas_do_usuario)
        
        apertar_Tab()
        escrever_texto(data_convertida)#aqui ele vai escrever a data de solicitação
        voltar_celula()
        mesclar_e_centralizar_celulas(quantidade_matriculas,cordenadas_do_usuario)
        
        apertar_Tab()
        escrever_texto(data_adcionada_7_dias)#aqui ele vai escrever a data de entrega
        voltar_celula()
        mesclar_e_centralizar_celulas(quantidade_matriculas,cordenadas_do_usuario)  
        
        apertar_Tab()
        escrever_texto("Rural")
        voltar_celula()
        mesclar_e_centralizar_celulas(quantidade_matriculas,cordenadas_do_usuario)
        
        apertar_Tab()
        escrever_texto(nome_proponente_geral)
        voltar_celula()
        mesclar_e_centralizar_celulas(quantidade_matriculas,cordenadas_do_usuario)
        
        apertar_Tab()
        escrever_texto(cidade)
        voltar_celula()
        mesclar_e_centralizar_celulas(quantidade_matriculas,cordenadas_do_usuario)
        
        apertar_Tab()
        for area in areas_matriculas:
            escrever_texto(area)#aqui digitando a area de matricula
            apertar_espaco()
            escrever_texto(' ha')
            time.sleep(0.2)
            enter()
            apertar_Tab()
        contornar_area()#contornando a area pra ela voltar pro inicio

        apertar_Tab()
        for i in range(5):#mesclando as colunas[quem marcou a vistoria,vistoriador,data da vistoria,responsavel pelo laudo]
            mesclar_e_centralizar_celulas(quantidade_matriculas,cordenadas_do_usuario)
            apertar_Tab()
        
        if possui_eml == 'Sim':
            escrever_texto(quem_vai_Receber_vistoriador)
            apertar_espaco()
            escrever_texto(telefone)
        else:
            escrever_texto(quem_vai_Receber_vistoriador)
        voltar_celula()
        mesclar_e_centralizar_celulas(quantidade_matriculas,cordenadas_do_usuario)
        apertar_Tab()
        apertar_home()

    if possui_eml == 'Sim':
        deletar_primeiro_eml()

    janela_dinamica('terminou sugira melhorias')