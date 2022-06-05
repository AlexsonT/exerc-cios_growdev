# 26) Escreva um programa que aceite uma quantidade de minutos e o converta em horas e dias. Por exemplo, 6.000 minutos equivalem a 100 horas e é igual a 4.167 dias

minutos = int(input('Quanto minutos quer converter? '))

horas = (minutos/60)
dias = (horas/24)

print(f'Essa quantia de minutos equivale a: {horas: .2f} horas e {dias: .2f} dias.')
