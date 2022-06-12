# 5) Construa um programa que permita a um usuário informar uma série de números, até que um número negativo seja fornecido. Ao final, imprima o somatório desses números, a média, o valor máximo e o mínimo. Desconsidere o último número (negativo) informado pelo usuário.
num = 0
lista = []

while num >= 0:
    num = int(input('Insira um número >= 0 para continuar ou < 0 para parar: '))
    lista.append(num)
    if num >= 0:
        soma = sum(lista)
        media = soma / len(lista)
        minimo = min(lista)
        maximo = max(lista)

print('-'*50)
print(f'A soma dos valores digitados é: {soma}')
print(f'A média dos valores digitado é: {media: .2f}')
print(f'O maior valor digitado foi: {maximo}')
print(f'O menor valor digitado foi: {minimo}')
print(f'Você digitou >> {num} << para parar o programa.')
print('-'*50)