# 9) Escreva um programa que receba o nome de 10 pessoas e para cada pessoa, o lugar para o qual ela já viajou. Sendo que existem 3 possibilidades:
# a) Rio de Janeiro
# b) Bahia
# c) Minas Gerais
# Após, informar qual foi o destino mais visitado e qual o menos visitado.

mais = menos = rj = ba = mg = 0
for n in range(10):
    nome = str(input('Insira seu nome: '))
    print('[1]RIO DE JANEIRO\n[2]BAHIA\n[3]MINAS GERAIS')
    local = int(input('Informe para quais destes destinos já viajou: '))
    print('.'*50)
    if local == 1:
        rj += 1
    elif local == 2:
        ba += 1
    else:
        mg += 1

print('.'*50)
if rj > ba and rj > mg:
    print('O Rio de Janeiro foi o local mais visitado!')
elif ba > rj and ba > mg:
    print('A Bahia foi o local mais visitado!')
elif mg > rj and mg > ba:     
    print('Minas Gerais foi o local mais visitado')
if mg == rj or mg == ba or ba == rj:
    print('Houve empate entre destinos!')    

if rj < ba and rj < mg:
    print('O Rio de Janeiro foi o local menos visitado!')
elif ba < rj and ba < mg:
    print('A Bahia foi o local menos visitado!')
elif mg < rj and mg < ba:     
    print('Minas Gerais foi o local menos visitado')
if mg == rj or mg == ba or ba == rj:
    print('Houve empate entre destinos!') 
print('.'*50)   
      