# 6) As reprovações são maiores entre os alunos do 1º, 2º ou 3º ano?. Crie um gráfico para mostrar isso.3

import csv
import matplotlib.pyplot as plt

with open('alunos.csv', 'r') as data_file:
    csv_reader = csv.reader(data_file)

    next(csv_reader)
    
    rep01 = []
    cont_rep01 = []
    rep02 = []
    cont_rep02 = []
    rep03 = []
    cont_rep03 = []
  
    for line in csv_reader:
        line[1] = int(line[1])
        line[6] = float(line[6])

        if line[6] <= 5 and line[6] > 0 and line[1] == 1:
            rep01.append([1])
            cont_rep01.append(len(rep01) + 1)
        if line[6] <= 5 and line[6] > 0 and line[1] == 2:
            rep02.append([2])
            cont_rep02.append(len(rep02) + 1)
        if line[6] <= 5 and line[6] > 0 and line[1] == 3:
            rep03.append([3])
            cont_rep03.append(len(rep03) + 1)

print(max(cont_rep01))
print(max(cont_rep02))
print(max(cont_rep03))
# print(rep02)
# print(rep03)
# soma = rep01 + rep02 + rep03
# print(soma)

plt.plot(cont_rep01, cont_rep02, cont_rep03)
plt.show()