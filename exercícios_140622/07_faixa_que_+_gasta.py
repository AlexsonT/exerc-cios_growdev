#7) Qual é a faixa etária que mais gasta?
import csv


with open('compras.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)

    # Jovens = 18 a 25 anos
    # Adultos, 26 a 59 anos
    # Idosos, igual ou maior que 60 anos

    soma1 = []
    soma2 = []
    soma3 = []
    jovens = adultos = idosos = 0

    for line in csv_reader:
        line[2] = int(line[2])
        line[4] = int(line[4])
        if line[2] >= 18 and line[2] < 26:
            jovens +=1
            soma1.append(line[4])
        elif line[2] >= 26 and line[2] < 60:
            adultos += 1
            soma2.append(line[4])
        else:       
            idosos += 1
            soma3.append(line[4]) 

print('*'*50)
print(f'Há {jovens} cadastros na faixa de jovens.')
print(f'Totalizando{sum(soma1): .2f} em gastos.')
print(f'Há {adultos} cadastros na faixa de adultos.')
print(f'Totalizando{sum(soma2): .2f} em gastos.')
print(f'Há {idosos} cadastros na faixa de idosos.')
print(f'Totalizando{sum(soma3): .2f} em gastos.')
print('*'*50)