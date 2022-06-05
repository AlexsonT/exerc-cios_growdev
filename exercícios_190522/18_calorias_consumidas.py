# 18)Um saco de biscoitos contém 40 unidades que, de acordo com as informações do rótulo, equivalem a 10 porções. Ainda de acordo com o rótulo, uma porção possui 300 calorias. Baseado nessas informações, crie um algoritmo que permita ao usuário inserir o número de biscoitos que ele consumiu e imprima na tela a quantidade de calorias correspondentes.

qtd = int(input('Insira a quantidade de biscoitos consumidos: '))

unical = 300/4
caltot = unical * qtd

print(f'Você comeu {qtd} biscoitos e o ingeriu um total de {caltot} calorias')