#15) Construa um algoritmo que, a partir de duas cores primárias fornecidas pelo usuário, determine qual cor seria obtida pela mistura delas. As cores vermelho, azul e amarelo são chamadas de cores primárias porque não podem ser obtidas a partir de outras cores e, quando misturadas, resultam numa cor secundária, de acordo com as seguintes regras:
#a) vermelho + azul = roxo;
#b) vermelho + amarelo = laranja;
#c) azul + amarelo = verde.
#Se o usuário inserir algo diferente de “vermelho”, “azul” ou “amarelo”, o programa deverá exibir uma mensagem de erro. Caso contrário, o programa deve exibir o nome da cor secundária resultante.
print('*'*50)
print('As cores primárias são: vermelho, azul e amarelo!')
print('>>>>>>  Utilize a tecla CAPSLOCK ativada!  <<<<<<')
print('*'*50)
cor = str(input('Informe uma cor primária:'))
while cor not in 'VERMELHO AZUL AMARELO ':
    print('Cor inválida, digite uma cor primária!') 
    cor = str(input('Informe uma cor primária:'))

cor2 = str(input('Informe outra cor primária:'))
while cor2 not in 'VERMELHO vermelho AZUL azul AMARELO amarelo':
    print('Cor inválida, digite uma cor primária!') 
    cor2 = str(input('Informe uma cor primária diferente'))

if cor == 'VERMELHO' and cor2 == 'AZUL':
    print('-'*50)
    print('Esta combinação resulta em:  ROXO')
    print('-'*50)
elif cor == 'AZUL' and cor2 == 'VERMELHO':
    print('-'*50)
    print('Esta combinação resulta em:  ROXO')
    print('-'*50)   
if cor == 'VERMELHO' and cor2 == 'AMARELO':
    print('-'*50)
    print('Esta combinação resulta em: LARANJA')
    print('-'*50)
elif cor == 'AMARELO' and cor2 == 'VERMELHO':
    print('-'*50)
    print('Esta combinação resulta em: LARANJA')
    print('-'*50)    
if cor == 'AZUL' and  cor2 == 'AMARELO':
    print('-'*50)
    print('Esta combinação resulta em: VERDE')
    print('-'*50)
elif cor == 'AMARELO' and  cor2 == 'AZUL':
    print('-'*50)
    print('Esta combinação resulta em: VERDE')
    print('-'*50)   