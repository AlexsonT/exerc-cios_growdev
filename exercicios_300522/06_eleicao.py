#6) Em uma eleição presidencial existem dois candidatos. Os votos são informados através de códigos. Os dados utilizados para a contagem dos votos obedecem à seguinte codificação:
#a) 1,2 = voto para os respectivos candidatos
#b) 3 = voto nulo
#c) 4 = voto em branco;
#Elabore um programa que leia o código de votação de 2 candidatos. Calcule e escreva:
#a) total de votos para cada candidato
#b) total de votos nulos
#c) total de votos em branco

cand01 = cand02 = nulo = branco = 0 
contagem = voto = 0
print('-'*50)
print('INFORME SUA OPÇÃO PARA PRESIDENTE DA EMPRESA ')
print('-'*50)
while voto != 5:
    print(' [1]candidato 01\n [2]candidato 02\n [3]nulo\n [4]branco\n [5]encerrar sessão')
    voto = int(input('Informe o número do seu candidato:'))
    contagem += 1
    print('-'*50)
    if voto == 1:
        cand01 += 1
    elif voto == 2:
        cand02 += 1
    elif voto == 3:
        nulo += 1
    elif voto == 4:
        branco += 1
print('='*50)         
print(f'O total de votos apurados foi de: {contagem-1} votos.')
print(f'O candidato 01 recebeu {cand01} votos.')
print(f'O candidato 02 recebeu {cand02} votos.')
print(f'Tivemos {nulo} votos nulos.')
print(f'Tivemos {branco} votos em branco.')
print('='*50)