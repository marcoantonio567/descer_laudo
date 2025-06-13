import pyautogui
import time
#importar pastas dentro de pastas
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from functions.manipular_textos.manipular_textos import verificar_se_Tem_textos
from functions.pyaytogui.funcoes_teclado_mouse import copiar,apertar_pra_baixo,enter,esquerda,direita,cima,apertar_Tab

def mesclar():
    pyautogui.keyDown('alt')
    pyautogui.keyDown('o')
    pyautogui.keyDown('m')
    pyautogui.keyDown('a')
    time.sleep(0.2)
    pyautogui.keyUp('alt')
    pyautogui.keyUp('o')
    pyautogui.keyUp('m')
    pyautogui.keyUp('a')

def centralizar_texto_meio():
    pyautogui.keyDown('alt')
    pyautogui.keyDown('o')
    pyautogui.keyDown('a')
    pyautogui.keyDown('m')
    time.sleep(0.2)
    pyautogui.keyUp('alt')
    pyautogui.keyUp('o')
    pyautogui.keyUp('a')
    pyautogui.keyUp('m')

def ir_pra_ultima_celula_da_coluna():
    #aqui ele vai verificar celula por celula ate encontrar a vazia
    pyautogui.hotkey('ctrl','down')
    copiar()
    last_cell = verificar_se_Tem_textos()
    while last_cell != False:
        apertar_pra_baixo()
        copiar()
        last_cell = verificar_se_Tem_textos()


def ir_pra_celula_A1():
    pyautogui.hotkey('ctrl','home')

def inserir_linhas_acima():
    pyautogui.keyDown('alt')
    pyautogui.keyDown('i')
    pyautogui.keyDown('r')
    
    time.sleep(0.1)
    pyautogui.keyUp('alt')
    pyautogui.keyUp('i')
    pyautogui.keyUp('r')
    time.sleep(0.1)
    enter()
    time.sleep(0.1)

def contornar_area():
    esquerda()
    pyautogui.hotkey('ctrl','up')
    apertar_pra_baixo()
    direita()
    
def voltar_celula():
    apertar_Tab()
    esquerda()

def visao_debaixo():
    pyautogui.hotkey('ctrl','down')
    pyautogui.hotkey('ctrl','up')
    apertar_pra_baixo()