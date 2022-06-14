# 3) Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string em um formato por extenso. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

import locale
from datetime import datetime

locale.setlocale(locale.LC_ALL, 'pt_BR')

def retorna_data_extenso(data_string):
    try:
        datetime.strptime(data_string, '%d/%m/%Y')
    except ValueError:
        print("Formato de data inválido, deve ser DD/MM/AAAA")
        return None 
    else:
        data_datetime = datetime.strptime(data_string, '%d/%m/%Y')
        return datetime.strftime(data_datetime, '%d de %B de %Y')
            
data = input("Digite uma data no formato DD/MM/AAAA:")
data_extenso = retorna_data_extenso(data)

if data_extenso is not None:
    print(data_extenso)