import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from functions.pyaytogui.funcoes_teclado_mouse import direita, apertar_pra_baixo , copiar , cima
from functions.pyaytogui.google_sheets_atalhos import ir_pra_ultima_celula_da_coluna , ir_pra_celula_A1 , inserir_linhas_acima
from functions.manipular_textos.manipular_textos import verificar_se_Tem_textos

def verificar_espaco_linha(quantidade_necessaria):
    if quantidade_necessaria >1:
        time.sleep(0.2)
        ir_pra_celula_A1()
        for i in range(4):#aqui to indo pra coluna "E" da planilha
            direita()
        time.sleep(0.2)

        ir_pra_ultima_celula_da_coluna()

        copiar()
        last_cell = verificar_se_Tem_textos()
        espaco_atual = 0 
        #aqui em baixo ele ta verificando o espaço atual
        while last_cell != True:
            apertar_pra_baixo()
            copiar()
            last_cell = verificar_se_Tem_textos()
            espaco_atual +=1
        
        cima()
        
        time.sleep(0.1)
        #inserindo linhas na planilha
        while espaco_atual<=quantidade_necessaria:
            inserir_linhas_acima()
            espaco_atual +=1
        
        ir_pra_celula_A1()#indo pra celula a1 indenpendente do resultado

time.sleep(3)
verificar_espaco_linha(5)
