#27) Conversão de graus Celsius para Fahrenheit – Crie um algoritmo que converta graus Celsius em Fahrenheit. A fórmula é a seguinte:
#F = 9/5C + 32
#O programa deve solicitar ao usuário que insira uma temperatura em graus Celsius e, em seguida, exiba a temperatura convertida em Fahrenheit. Após construir esse algoritmo, modifique-o para que converta graus Fahrenheit em graus Celsius.

print("Informe a temperatura em graus Celsius: ")
celsius = int(input())

fahrenheit = 9 / 5 * celsius + 32

print(f'Temperatura em Fahrenheit: {fahrenheit}.')

# formato 2
print("Informe a temperatura em graus Fahrenheit: ")
celsius = int(input())

celsius = (fahrenheit - 32) * 5 / 9

print(f'Temperatura em Celsius: {celsius}.')