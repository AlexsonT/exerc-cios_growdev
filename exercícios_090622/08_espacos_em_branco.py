# 8) Escreva uma função que conte o número de espaços em branco em uma frase passada como parâmetro.

# def contador_de_espacos():
#     frase = str(input('Insira uma frase para contarmos os espacos: '))
#     espacos = frase.count(' ')
#     print(f'Sua frase tem {espacos} espaços.')
    
# contador_de_espacos()      

# frase = input('Insira uma frase:')

# def contador_de_espacos(frase):
#     espacos = 0
#     for letter in frase:
#         if letter == None:
#             espacos += 1
#     print(espacos)

# contador_de_espacos(frase)

def contador_de_espacos():
    frase = str(input('Insira uma frase para contarmos os espacos: '))
    caracteres = len(frase)
    espacos = frase.count(' ') 
    contador = (caracteres - espacos)
    print(f'Sua frase tem {espacos} espaços.')
    print(caracteres)
    print(espacos)    
contador_de_espacos() 