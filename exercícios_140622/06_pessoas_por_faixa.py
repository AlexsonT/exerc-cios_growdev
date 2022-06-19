#6) Utilizando as faixas etárias, diga quantas pessoas há em cada faixa?

import csv


with open('compras.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    # Jovens = 18 a 25 anos
    # Adultos, 26 a 59 anos
    # Idosos, igual ou maior que 60 anos

    jovens = adultos = idosos = 0

    for line in csv_reader:
        line[2] = int(line[2])
        if line[2] >= 18 and line[2] < 26:
            jovens +=1
        elif line[2] >= 26 and line[2] < 60:
            adultos += 1
        else:       
            idosos += 1

print('*'*50)
print(f'Há {jovens} cadastros na faixa de jovens.')
print(f'Há {adultos} cadastros na faixa de adultos.')
print(f'Há {idosos} cadastros na faixa de idosos.')
print('*'*50)