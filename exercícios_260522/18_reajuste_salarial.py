#18)As Organizações XTC resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calcula os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#a) salários até R$ 280,00 (incluindo): aumento de 20%
#b) salários entre R$ 280,00 e R$ 700,00: aumento de 15%
#c) salários entre R$ 700,00 e R$ 1500,00: aumento de 10%
#d) salários de R$ 1500,00 em diante: aumento de 5% 

#Após o aumento ser realizado informe na tela:
#a) o salário antes do reajuste;
#b) o percentual de aumento aplicado;
#c) o valor do aumento;
#d) o novo salário, após o aumento.

sal = float(input('Informe o salário a reajustar: R$ '))

if sal <= 280:
    print('='*50)
    print(f'Salário a reajustar: R$ {sal: .2f}')
    print('Reajuste de 20%')
    print(f'O aumento é de: R${sal*.2: .2f}')
    print(f'O novo salário é: R${sal*1.2: .2f}.')
    print('='*50)
if sal >280 and sal <=700:
    print('='*50)
    print(f'Salário a reajustar: R$ {sal: .2f}.')
    print('Reajuste de 15%')
    print(f'O aumento é de: R${sal*.15: .2f}.')
    print(f'O novo salário é: R${sal*1.15: .2f}.')
    print('='*50)
if sal >700 and sal <=1500:
    print('='*50)
    print(f'Salário a reajustar: R$ {sal: .2f}.')
    print('Reajuste de 10%')
    print(f'O aumento é de: R${sal*.1: .2f}.')
    print(f'O novo salário é: R${sal*1.1: .2f}.')
    print('='*50)
if sal >1500:   
    print('='*50) 
    print(f'Salário a reajustar: R$ {sal: .2f}')
    print('Reajuste de 5%')
    print(f'O aumento é de: R${sal*.05: .2f}.')
    print(f'O novo salário é: R${sal*1.05: .2f}.')
    print('='*50)