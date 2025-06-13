import pyautogui
import time

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from functions.outras_funcoes.distancia import converter_pixels
from functions.pyaytogui.google_sheets_atalhos import mesclar , centralizar_texto_meio

def mesclar_e_centralizar_celulas(quantidade_celulas,resolucao=()):
    time.sleep(0.5)
    # Cor alvo (R, G, B)
    target_color = (26, 115, 232)

    # Deslocamento desejado após encontrar a cor
    offset_x = 10  # direita
    offset_y = 5   # baixo

    def encontrar_cor_na_tela(cor):
        screenshot = pyautogui.screenshot()
        width, height = screenshot.size

        for x in range(width):
            for y in range(height):
                pixel = screenshot.getpixel((x, y))
                if pixel == cor:
                    return x, y
        return None

    # Espera um segundo para o usuário preparar a tela
    

    # Procurar e clicar
    pos = encontrar_cor_na_tela(target_color)
    if pos:
        ajustado = (pos[0] + offset_x, pos[1] + offset_y)
        pyautogui.moveTo(ajustado[0], ajustado[1],duration=0.3)
        pixel_convertido = converter_pixels(19,eixo='y',resolucao_nova=(resolucao[0],resolucao[1]))
        #mover pra segunda tela
        celula = pixel_convertido*quantidade_celulas #px
        new_y = ajustado[1] + celula #soma o valor que ja tava no y com a quantidade de celulas pra mesclar
        pyautogui.mouseDown()  # Pressiona o botão esquerdo
        pyautogui.moveTo(ajustado[0], new_y, duration=1)  # Arrasta até a nova posição
        pyautogui.mouseUp()  # Solta o botão do mouse
        time.sleep(0.2)
        mesclar()
        time.sleep(0.2)
        centralizar_texto_meio()
        time.sleep(0.2)
        #mesclar celulas --> lower
        #alinhamento de texto: meio --> lower
    else:
        print("Cor não encontrada na tela.")

#mesclar_e_centralizar_celulas(4,resolucao=(1366,768))