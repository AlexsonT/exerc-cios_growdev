#1) Procure quem foi a pessoa que mais gastou?

#importing csv default and reading the informations of archive.
import csv

nome_arquivo = 'compras.csv'
f = open(nome_arquivo, encoding='utf-8')
dados = csv.reader(f, delimiter=',')
dados = list(dados)


#converting data type from str to int.
quantidade_registros = len(dados)

for i in range(1, quantidade_registros):
    dados[i][2] = int(dados[i][2])
    dados[i][4] = int(dados[i][4])
    dados[i][5] = int(dados[i][5])

#traversing the lines and looking for the highest value.
maior_compra = -1
indice_maior_compra = 0
info = dados[1:]
cabecalho = dados[0]

for indice, linha in enumerate(info):
    if linha[4] > maior_compra:
        maior_compra = linha[4]
        indice_maior_compra = indice

pessoa = info[indice_maior_compra]

print('*'*50)
print(f'{pessoa[0]} {pessoa[1]}')
print('*'*50)
#the name found was 'Gabriel Pereira'.