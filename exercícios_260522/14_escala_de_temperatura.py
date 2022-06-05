#14) Faça um algoritmo para ler a temperatura atual e conforme leitura, imprima o resultado de acordo com a tabela abaixo.
# Temperatura Resultado / até 15o Muito frio / de 16o à 22o Frio / de 23o à 26o Agradável / de 27o à 30o Quente / 31o ou mais Muito quente.

temp = float(input('Insira a temperatura a avaliar em °C: '))


if temp <= 15.0:
    print('MUITO FRIO')
elif temp > 15 and temp <=22:
    print('FRIO')
elif temp > 22 and temp <=26:
    print('AGRADÁVEL')
elif temp > 26 and temp <=30:
    print('QUENTE')
elif temp > 30:
    print('MUITO QUENTE')    