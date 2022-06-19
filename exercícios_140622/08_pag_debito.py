# 8) A opção de débito é mais utilizada entre homens ou mulheres?

import csv

with open('compras.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    debitom = debitof = 0
    
    for line in csv_reader:
        if line[3] == 'M':
            if line[6] == 'debito':
                debitom += 1
        if line[3] == 'F':
            if line[6] == 'debito':
                debitof += 1

print('='*50)
print(f'A quantidade de homens que utilizaram a opção débito foi de: {debitom}.')
print(f'A quantidade de mulheres que utilizaram a opção débito foi de: {debitof}.')

print('.'*50)
if debitom > debitof:
    print('Os homens utilizaram a opção débito mais vezes.')
elif debitof > debitom:
    print('As mulheres utilizaram a opção débito mais vezes.')
else:        
    print('Ambos utilizaram a opção débito na mesma proporção')
print('='*50)    

