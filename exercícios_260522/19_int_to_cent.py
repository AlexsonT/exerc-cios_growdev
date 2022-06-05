#19) Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo. Exemplos: 326 = 3 centenas, 2 dezenas e 6 unidades 12 = 1 dezena e 2 unidades

num = int(input('Insira um número inteiro até 1000: '))

while num <= 0 or num > 1000:
    print('Número inválido!')
    num = int(input('Insira um número inteiro até 1000: '))

centenas = num / 100
centenas = centenas - centenas % 1

num = num - centenas * 100

dezenas = num / 10
dezenas = dezenas - dezenas % 1

unidades = num - dezenas * 10

print(f'Centenas: {centenas}\nDezenas: {dezenas}\nUnidades: {unidades}.')