import pyautogui
import keyboard
import time
import openpyxl
import pyperclip


def enter():
    pyautogui.press("enter")
def tempo():
    time.sleep(0.2)
def tab():
    pyautogui.press("tab")
def f6():
    pyautogui.press('f6')
def colar():
    pyautogui.hotkey("ctrl","v")
pyautogui.alert("abra o arcmap")

planilha = openpyxl.load_workbook('coordenadas_extraidas (MAT. 52).xlsx')
pagina = planilha['Sheet1']

for linha in pagina.iter_rows(min_row=2,values_only=True):
    longitude = linha[0]
    latitude = linha[1]
    longitude = longitude.replace('-' , '')
    latitude = latitude.replace('-' , '')
    print(f'LONG : {longitude}')
    print(f'LAt : {latitude}')
    tempo()
    pyperclip.copy(longitude)
    f6()
    colar()#aqui vai colar a long
    pyperclip.copy("")
    pyautogui.press('W')
    tab()
    pyperclip.copy(latitude)
    colar()#aqui vai colar a lat
    pyautogui.press('S')
    pyperclip.copy("")
    tempo()
    enter()

