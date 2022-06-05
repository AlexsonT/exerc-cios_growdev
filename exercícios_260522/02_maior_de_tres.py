# 2) Escreva um algoritmo que leia 3 valores e exiba qual o maior valor entre eles.
val01 = float(input('Insira o primeiro valor: '))
val02 = float(input('Insira o segundo valor: '))
val03 = float(input('Insira o terceiro valor: '))

if val01 > val02 and val01 > val03:
    print(f'{val01} é o maior valor entre a amostra!')
elif val02 > val01 and val02 > val03:
    print(f'{val02} é o maior valor entra a amostra!')
elif val03 > val01 and val03 > val02:
    print(f'{val03} é o maior valor entre a amostra!')
else:
    print('Há dois valores iguais no maior valor da amostra!')
