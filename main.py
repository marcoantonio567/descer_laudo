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
from functions.precessamento.rural.processar_rural import *

instituicao = selecionar_resposta("Selecione qual a instituição",[
    "Sicredi",
    "Banco da Amazônia",
    "BRB",
    "Pericia",
    "Particular",
    "Sicoob TO",
    "Sicoob Uni",
    "Caixa",
])


gerenciar_rurais(instituicao=instituicao)

    
    