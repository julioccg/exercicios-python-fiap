nome = str(input('Nome: '))
idade = int(input('Idade: '))
doenca_infectocontagiosa = input('Suspeita de doença infecto-contagiosa? [S/N] ').upper().strip()[0]
#PRIMEIRO PROBLEMA A SER RESOLVIDO
if doenca_infectocontagiosa == 'S':
    print('Encaminhe o paciente para a SALA AMARELA')
elif doenca_infectocontagiosa == 'N':
    print('Encaminhe o paciente para a SALA BRANCA')
else:
    print('RESPONDA COM SIM OU NÃO')

#SEGUNDO PROBLEMA A SER RESOLVIDO
if idade >= 65:
    print('Paciente COM PRIORIDADE')
else:
    genero  = input('Digite o gênero do paciente: ').upper()
    if genero == 'FEMININO' and idade > 10:
        gravidez = input('A paciente está grávida? ').upper()
        if gravidez == 'SIM':
            print('Paciente COM priorodade')
        else:
            print('Paciente SEM prioridade')
    else:
        print('Paciente SEM prioridade')