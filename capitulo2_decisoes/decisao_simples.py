nome = str(input('Nome: '))
idade = int(input('Idade: '))
prioridade = str('NÃO')
if idade >= 65:
    prioridade = 'SIM'
print(f'O paciente {nome} possui atendimento prioritário? {prioridade}')