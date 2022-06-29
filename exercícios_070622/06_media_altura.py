# 6) Crie um programa que leia continuamente a altura e o sexo de uma lista de pessoas salvando todas as informações em listas, até que uma altura negativa seja fornecida. Ao final, sabendo que a média de altura para as mulheres brasileiras é de 1.60m e a dos homens brasileiros é de 1.73m, escreva as seguintes informações:
# a) quantas mulheres da lista estão acima da média nacional de altura para mulheres, e quantas estão abaixo;
# b) quantos homens da lista estão acima da média nacional de altura para homens, e quantos estão abaixo.

altura = []
sexo = []
a = altura_m_maior = altura_m_menor = altura_f_maior = altura_f_menor = 0
while a >= 0:
    a = float(input('Insira uma altura:'))
    if a >=0:
        s = input('Insira [M] se for Masculino ou [F] se Feminido:')
        if a >= 0:
            altura.append(a)
            sexo.append(s)
        if s == 'M' or s == 'm' and a > 1.73:
            altura_m_maior += 1
        elif s == 'M' or s == 'm' and a <= 1.73:
            altura_m_menor += 1

        if s == 'F' or s == 'f' and a > 1.6:
            altura_f_maior += 1
        elif s == 'F' or s == 'f' and a <= 1.6:
            altura_f_menor += 1
    else:
        break        
print('.'*50)
print(f'Quantidade de homens acima da média: {altura_m_maior}.')
print(f'Quantidade de homens abaixo da média: {altura_m_menor}.')  
print(f'Quantidade de mulheres acima da média: {altura_f_maior}.')
print(f'Quantidade de mulheres abaixo da média: {altura_f_menor}.')  
print(altura, sexo)
print('.'*50)