from datetime import datetime , timedelta
import pyperclip

def converter_data(data_str):
    meses = {
        "jan": "01", "fev": "02", "mar": "03", "abr": "04",
        "mai": "05", "jun": "06", "jul": "07", "ago": "08",
        "set": "09", "out": "10", "nov": "11", "dez": "12"
    }
    
    partes = data_str.lower().split(" de ")
    dia = partes[0].zfill(2)
    mes = meses.get(partes[1], "00")
    ano = partes[2]
    
    return f"{dia}/{mes}/{ano}"
def adicionar_7_dias(data_str):
    # Converte a string para um objeto datetime
    data = datetime.strptime(data_str, "%d/%m/%Y")
    
    # Adiciona 7 dias
    nova_data = data + timedelta(days=7)
    
    # Retorna a nova data formatada
    return nova_data.strftime("%d/%m/%Y")


def verificar_se_Tem_textos():
    # Verifica se tem texto na area de trasferencia se tiver retornar true se não tiver retorna false
    conteudo = pyperclip.paste()
    if conteudo.strip() == "":
        return False
    else:
        return True
