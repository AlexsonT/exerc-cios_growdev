#2) Escrever um programa que lê um valor N inteiro e positivo e que calcula seu valor fatorial. Ex: 5! = 5 * 4 * 3 * 2 * 1

n = int(input('Insira um valor inteiro e positivo: '))

f = 1
while (n > 1):
    f = f * n
    n = n - 1
print(f'O valor fatorial é {f}!')

#valor = int(input('Entre com um número para saber o fatorial:'))  
#fatorial = 1  
#while (valor > 1):  
#  fatorial = fatorial * valor  
#  valor = valor - 1  
#print('O fatorial é {}.'.format(fatorial))