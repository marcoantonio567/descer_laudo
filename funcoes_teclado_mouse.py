import webbrowser
import pyautogui
import keyboard
import time

def abrir_link(url):
    webbrowser.open(url)

def janela_dinamica(texto = 'Pressione OK para continuar'):
    pyautogui.alert(texto)

def clicar_centro_tela():
    pyautogui.click(pyautogui.size()[0]//2,pyautogui.size()[1]//2,duration=0.25)

def ir_pra_celula_A1():
    pyautogui.hotkey('ctrl','home')


def apertar_pra_baixo():
    pyautogui.press('down')


def apertar_home():
    pyautogui.press('home')

def ir_pra_ultima_celula_da_coluna():
    pyautogui.hotkey('ctrl','down')

def apertar_Tab():
    pyautogui.press('tab')
    time.sleep(0.3)
def escrever_texto(texto):
    keyboard.write(texto,delay=0.01)

def apertar_espaco():
    pyautogui.press('space')