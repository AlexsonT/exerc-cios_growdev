#3) Escrever um programa que lê um valor N inteiro e positivo e que calcula e escreve o valor de E.
#E = 1 + 1 / 1! + 1 / 2! + 1 / 3! + ... + 1 / N!


# adicao = soma = n = 0
# while adicao != 2:
#     print('-*'*25)
#     n = int(input('Insira um número inteiro: '))
#     print(' [1] Adicionar + valor\n [2] Parar')
#     adicao = int(input('Insira uma opção: '))
#     soma += n
# print('='*50)    
# print(f'O valor de E é {soma}')   
# print('='*50)

n = int(input("Informe um número: "))

valor_e = 1

for i in range(1, n + 1):

    fatorial = 1
    for j in range(i, 1, -1):
        fatorial = fatorial * j
    
    valor_e += 1 / fatorial

print(f"E: {valor_e}")
