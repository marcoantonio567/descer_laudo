import pyautogui

def converter_cordenadas(x_base,y_base):
    """Essa função basicamente recebe a cordenada de onde voce deveria clicar como parametro
    e passa as resposta como se fosse pra aplicar com a tela 1366X768
    O output da função vai ser uma tupla com  as coordenadas certas"""
    # Resolução base (a que você usou para mapear as coordenadas)
    base_width = 1366
    base_height = 768

    # Pega a resolução atual do monitor
    current_width, current_height = pyautogui.size()

    # Aplica a regra de três para escalar as coordenadas
    x_real = int((x_base / base_width) * current_width)
    y_real = int((y_base / base_height) * current_height)

    return x_real,y_real

