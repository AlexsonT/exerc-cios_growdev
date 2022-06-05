#8) Um carpinteiro esculpe placas personalizadas para estabelecimentos comerciais e deseja um programa que faça orçamentos das placas que produz, considerando as seguintes informações:
#a) O valor mínimo de qualquer placa é de R$ 300,00;
#b) Placas de angelim custam R$ 150,00 adicionais, mas placas de pinus não possuem nenhum custo extra;
#c) Frases com até 12 caracteres estão incluídas no valor mínimo; para frases maiores, são cobrados R$ 15,00 por caractere;
#d) Para placas com dizeres brancos ou pretos não se cobra adicional, mas se ele contiver letras douradas, cobra-se R$ 60,00 a mais.
#Baseado nessas informações, construa um algoritmo que leia o número de um orçamento, o nome do cliente, tipo de madeira (angelim ou pinus), número de caracteres da mensagem e a cor dos caracteres (branco, preto ou dourado). Ao final, imprima todos os dados de entrada e o preço da placa orçada.

#Valor mínimo 300 Pinus frases até 12 caract brancos ou pretos
# Angelim +150
#frases >12 caract 15,00 por caract
# douradas + 60,00
from time import sleep
print('-'*50)
print('OBS: UTILIZE A TECLA CAPSLOCK ATIVADA!')
print('-'*50)
nome = str(input('Nome do cliente: ')) 
tipo = str(input('ANGELIM PU PINUS?: '))
frase = str(input('QUAL A FRASE DA PLACA?: '))
print('-'*50)
print('Escolha o nº da cor entre as opções:')
print('Digite [1] para preto;')
print('Digite [2] para branco;')
print('Digite [3] para dourado;')
cor = int(input('Nº da cor: '))
print('-'*50)
caract = len(frase.replace(' ', ''))

if tipo == 'PINUS':
    orc = 300
else :
    orc = 450
if caract > 12:
    orc = orc + (15 * (caract - 12))
if cor == 3:
    orc = orc + 60
       
if cor == 1:
    cor_escolhida = 'PRETO'
elif cor == 2:
    cor_escolhida = 'BRANCO'
elif cor == 3:
    cor_escolhida = 'DOURADO'
else:
    cor_escolhida = 'COR INDEFINIDA'       

sleep(.5)
print('*'*50)
print('ORÇAMENTO >>>>> PLACAS DE MADEIRA DO ZÉ ME <<<<<')
print('*'*50)
print(f'CLIENTE: {nome}')
print(f'MADEIRA ESCOLHIDA: {tipo}')
print(f'FRASE ESCOLHIDA: {frase}')
print(f'QTD. CARACTERES: {caract} caracteres')
print(f'COR ESCOLHIDA: {cor_escolhida}')
print('.'*50)
print(f'VALOR TOTAL DO ORÇAMENTO: R$ {orc: .2f}')
print('.'*50)
print('*'*50)