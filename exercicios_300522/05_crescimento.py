#5) Chico tem 1,50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1,10 metro e cresce 3 centímetros por ano. Construa um programa que calcule e imprima quantos anos serão necessários para que Zé seja maior que Chico.

tempo = 0
ze = 1.1
chico = 1.5
while ze <= chico:
    ze += .3
    chico += .2
    tempo += 1
print('*'*50)
print(f'Zé levará {tempo} anos para ficar maior que Chico!')
print(f'Após esse período, Chico tera {chico: .2f}m e Zé terá{ze: .2f}m.')
print('*'*50)