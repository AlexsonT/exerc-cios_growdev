# 22) Uma receita de biscoitos exige os seguintes ingredientes para produzir 48 unidades:
# a) 1,5 xícaras de açúcar
# b) 1 xícara de manteiga
# c) 2,75 xícaras de farinha
# Crie um algoritmo que pergunte ao usuário quantos biscoitos ele deseja fazer e calcule a quantidade correspondente dos ingredientes.

acucar = 1.5/48
manteiga = 1/48
farinha = 2.75/48

qtd = int(input('Quantos biscoitos deseja produzir? '))

print('Você vai precisar de: ')
print(f'{acucar*qtd} xícaras de açucar')
print(f'{manteiga*qtd} xícaras de manteiga')
print(f'{farinha*qtd} xícaras de farinha')