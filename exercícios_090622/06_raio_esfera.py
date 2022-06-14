# 6) Escreva um programa para solicitar ao usuário o raio r de uma esfera, e calcular o volume V da esfera usando uma função, e exibir o resultado. Utilize  a seguinte fórmula para determinar o volume:
#v = (4.0 / 3.0) * π * r3

def volume():
    print('Cálculo do volume de uma esfera.')
    r = float(input('Informe o valor do Raio: '))    
    while r <= 0:
        print('Insira um valor positivo e válido para cálculo.')
        r = float(input('Informe o valor do Raio: '))  
    v = ((4 * 3.1416) * (r ** 3)) / 3   
    print(f'O valume da esfera é: {v: .2f} m³')

volume()

