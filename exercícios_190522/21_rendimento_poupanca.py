#21) Uma pessoa resolveu fazer uma aplicação em uma poupança programada. Para calcular seu rendimento, ela deverá fornecer o valor constante da aplicação mensal, a taxa e o número de meses. Sabendo-se que a fórmula usada para este cálculo é: P*(1+i)²-1 / i
#i = taxa
#P = aplicação
# n = número de meses

i = float(input('Forneça a taxa de correção: '))
p = float(input('Forneça o valor mensal aplicado: '))
n = int(input('Forneça o perído da aplicação em meses: '))

rend = i/100
calc = p * (((1 + rend)**n) - 1) / rend

print(f'O valor total de sua aplicação após {n} mêses será de ${calc: .2f} com rendimento de ${calc-(p*n): .2f}.')