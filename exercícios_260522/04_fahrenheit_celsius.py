# 4) Escreva um algoritmo para ler uma temperatura em graus Fahrenheit, calcular e escrever o valor correspondente em graus Celsius (baseado na fórmula abaixo):
# C/5 = F-32/9

temp = float(input('Insira a temperatura em °F: '))

print(f'A temperatura em Celsius é de {(temp-32) * 5/9}°C')
