import webbrowser
import pyautogui
import keyboard
import time
#importar pastas dentro de pastas
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


def abrir_link(url):
    webbrowser.open(url)

def janela_dinamica(texto = 'Pressione OK para continuar'):
    pyautogui.alert(texto)

def clicar_centro_tela():
    pyautogui.click(pyautogui.size()[0]//2,pyautogui.size()[1]//2,duration=0.25)

def apertar_pra_baixo():
    pyautogui.press('down')

def apertar_home():
    pyautogui.press('home')
      
def apertar_Tab():
    pyautogui.press('tab')
    time.sleep(0.3)

def escrever_texto(texto):
    keyboard.write(texto,delay=0.01)

def apertar_espaco():
    pyautogui.press('space')

def copiar():
    pyautogui.hotkey('ctrl','c')

def enter():
    pyautogui.press('enter')

def esquerda():
    pyautogui.press('left')

def direita():
    pyautogui.press('right')

def cima():
    pyautogui.press('up')

