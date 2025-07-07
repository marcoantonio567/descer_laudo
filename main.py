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
from functions.tkinter.fazer_campos_dinamicos import *
from functions.tkinter.campo_dinamico_opcoes import *
from functions.tkinter.formulario import *
from functions.tkinter.step_to_step import *
from functions.precessamento.rural.processar_rural import *
from functions.precessamento.urbano.processar_urbano import *
from functions.precessamento.maquinario.processar_maquinario import *

passo_passo()#mostrar o passo a passo
instituicao = selecionar_resposta("Selecione qual a instituição",[
    "Sicredi",
    "Banco da Amazônia",
    "BASA",
    "BRB",
    "Pericia",
    "Particular",
    "Sicoob TO",
    "Sicoob Uni",
    "Caixa",
])

tipo_laudo = selecionar_resposta("Selecione qual o tipo de laudo",["Rural","Urbano","Maquinario"])
if tipo_laudo == 'Rural':
    gerenciar_rurais(instituicao=instituicao)
if tipo_laudo == 'Urbano':
    gerenciar_Urbano(instituicao=instituicao)
if tipo_laudo == 'Maquinario':
    gerenciar_maquinario(instituicao=instituicao)
    
    