# 7) Faça uma função que recebe por parâmetro o tempo de duração da produção de uma peça em uma fábrica expressa em segundos e exibe esse tempo em horas, minutos e segundos.

def tempo_de_producao():
    segundos = int(input('Insira o tempo de produção em segundos: '))
    if segundos < 60:
        print(f'Você levou {segundos} segundos para produzir a peça X.')
    elif segundos < 3600:
        s = segundos % 60
        m = (segundos - s) / 60   
        print(f'Você levou{m} minutos e {s} segundos para produzir a peça X.')
    else:
        s = segundos % 60
        m = ((segundos - s) / 60) % 60
        h = ((segundos) / 3600) % 3600
        print(f'Você levou {h: .0f} horas, {m} minutos e {s} segundos para produzir a peça X.')
       
tempo_de_producao()    