# 12) A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,...Faça um programa capaz de gerar a série até o n−ésimo termo.


ultimo = int(input('Insira o último número da série de Fibonacci: '))

inicio = 0
atual = 1
fibonacci = 0
print('1')
while fibonacci < ultimo:
    fibonacci = inicio + atual
    inicio = atual
    atual = fibonacci
    print(fibonacci)

