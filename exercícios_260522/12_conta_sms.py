#12) Uma certa operadora de telefonia móvel cobra R$ 5,00 mensais pelo seu plano básico de transmissão de SMS (mensagens de texto), sendo que taxas adicionais são cobradas conforme as regras abaixo:
#a) As primeiras 60 mensagens estão incluídas no plano básico;
#b) Se o usuário mandar mais de 60 mensagens, cada mensagem adicional custará R$ 0.05, até o limite de 180 mensagens.
#c) Acima de 180 mensagens, o valor de cada uma delas passa a R$ 0,10;
#d) A soma dos impostos estaduais e federais amonta a 12% do valor de cada fatura.
#Com base nessas informações, crie um algoritmo para ler o número total de mensagens enviadas por um usuário. Ao final, calcule o valor da conta e mostre todos os dados, incluindo o valor da conta com e sem impostos.
print('='*50)
cliente = str(input('Qual o nome do cliente?: '))
sms = int(input('Quantos SMS foram enviados?: '))
print('='*50)
plano_basico = 5.0
print('FATURA DE SMS (OPERADORA MELHOR QUE CARTA BRASIL)')
print('='*50)

print(f'CLIENTE:{cliente}')
print(f'SMS NO PERÍODO: {sms}')


if sms <= 60:
    soma = plano_basico
    print(f'{sms} sem custo (Incluso em seu Plano).')
if sms > 60 and sms <= 180:
    soma = plano_basico + (sms - 60) * .05
    print('60 ... SMS sem custo (Incluso em seu Plano).')
    print(f'{sms-60: 2} SMS com custo adicional de R$ 0,05un.')
    print(f'------ Adicional de R$ {(sms-60) * .05} ------')
if sms > 180:
    soma = plano_basico + (120 *.05) + (sms - 180) * .10
    print('60 ... SMS sem custo (Incluso em seu Plano).')
    print('120 ... SMS com custo adicional de R$ 0,05 un.')
    print(f'------ Adicional de R$ {120 * .05: .2f} ------')
    print(f'{sms-180} ... SMS com custo adicional de R$0,10un.')
    print(f'------ Adicional de R$ {(sms-180) * .10: .2f} ------')
print('.'*50)
print(f'Total da fatura sem impostos R$ {soma: .2f}')
print(f'Total dos impostos: R${soma*.12: .2f}') 
print('*'*50)
print(f'>>>>>>>>>> TOTAL A PAGAR: R$ {soma*1.12: .2f} <<<<<<<<<<')
print('*'*50)