#30) Ler um número inteiro (assuma até três dígitos) e imprimir a saída da seguinte forma:
#CENTENA = x
#DEZENA = x
#UNIDADE = x
#Exemplo: 357 tem 3 centenas, 5 dezenas e 7 unidades.


num = int(input('Informe um número'))

centenas = num / 100
centenas = centenas - centenas % 1

num = num - centenas * 100

dezenas = num / 10
dezenas = dezenas - dezenas % 1

unidades = num - dezenas * 10

print(f'Centenas: {centenas}\nDezenas: {dezenas}\nUnidades: {unidades}.')