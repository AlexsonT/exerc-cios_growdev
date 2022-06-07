#17) Receba 3 notas de um aluno e peça o peso (em porcentagem) respectivamente de cada nota, ao final exiba a nota final do mesmo.

n1 = float(input('Insira a primeira nota do aluno: '))
n2 = float(input('Insira a segunda nota do aluno: '))
n3 = float(input('Insira a terceira nota do aluno: '))

soma = n1+n2+n3

print('='*50)
print('O RESULTADO DO ALUNO FOI')
print('='*50)
print(f'Nota 01 = {(n1/soma)*100: .2f}')
print(f'Nota 02 = {(n2/soma)*100: .2f}')
print(f'Nota 03 = {(n3/soma)*100: .2f}')
print(f'Sua média geral ficou em: {(soma/3): .2f}')
print('='*50)