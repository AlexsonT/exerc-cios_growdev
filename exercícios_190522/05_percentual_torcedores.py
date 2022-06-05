# 5) Escreva um programa que receba como entrada a quantidade de torcedores do time X, do time Y e do time Z, calcula e exibe qual a porcentagem de torcedores de cada time.
x = int(input('Há quantos torcedores do time x?'))
y = int(input('Há quantos torcedores do time y?'))
z = int(input('Há quantos torcedores do tome z?'))

total_torcedores = x + y + z
perc_x = (
    f'O percentual de tocedores torcendo para o time X é de: {(x/total_torcedores)*100} % de um total de {total_torcedores} torcedores!')
perc_y = (
    f'O percentual de tocedores torcendo para o time Y é de: {(y/total_torcedores)*100} % de um total de {total_torcedores} torcedores!')
perc_z = (
    f'O percentual de tocedores torcendo para o time Z é de: {(z/total_torcedores)*100} % de um total de {total_torcedores} torcedores!')
print(perc_x)
print(perc_y)
print(perc_z)
