# 3) Um brechó revende produtos usados, e fixa o preço de venda de cada produto conforme o valor de sua aquisição. Se o preço de aquisição de um produto é menor do de R$ 50.00, ele deve ser vendido por um preço 45% maior; caso contrário, o lucro será de 30%. Sabendo disso, construa um algoritmo que leia o valor de aquisição de um produto e mostre o seu valor de venda.

valorcompra = float(input("Insira o valor de compra do item: "))

if(valorcompra < 50.00):
    print(f'O valor de revenda do item é: R$ {valorcompra*1.45:.2f}')
else:
    print(f'O valor de revenda do item é: R$ {valorcompra*1.3:.2f}')
