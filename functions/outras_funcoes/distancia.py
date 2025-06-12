import math

def distancia_entre_pontos(p1, p2):
    """
    Calcula a distância entre dois pontos (x1, y1) e (x2, y2).
    
    Parâmetros:
    - p1: tupla (x1, y1)
    - p2: tupla (x2, y2)
    
    Retorna:
    - Distância em pixels (float)
    """
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def converter_pixels(px_original, eixo='x', resolucao_original=(1366, 768), resolucao_nova=(1920, 1080)):
    """
    Converte a quantidade de pixels proporcionalmente entre duas resoluções de tela.
    
    Parâmetros:
        px_original (int): valor em pixels na resolução original.
        eixo (str): 'x' para largura, 'y' para altura.
        resolucao_original (tuple): resolução base (largura, altura).
        resolucao_nova (tuple): nova resolução alvo (largura, altura).
    
    Retorno:
        int: valor em pixels correspondente na nova resolução.
    """
    if eixo == 'x':
        proporcao = resolucao_nova[0] / resolucao_original[0]
    elif eixo == 'y':
        proporcao = resolucao_nova[1] / resolucao_original[1]
    else:
        raise ValueError("Eixo deve ser 'x' ou 'y'.")

    return int(px_original * proporcao)

