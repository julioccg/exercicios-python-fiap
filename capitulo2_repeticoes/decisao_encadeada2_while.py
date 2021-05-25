resp = 'S'
while resp == 'S':
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    doenca_infectocontagiosa = input('Suspeita de doença infecto-contagiosa? [S/N] ').upper().strip()[0]
    while doenca_infectocontagiosa != 'S' and doenca_infectocontagiosa != 'N':
        doenca_infectocontagiosa = input('Suspeita de doença infecto-contagiosa? [S/N] ').upper().strip()[0]
    #PRIMEIRO PROBLEMA A SER RESOLVIDO
    if doenca_infectocontagiosa == 'S':
        print('Encaminhe o paciente para a SALA AMARELA')
    else:
        print('Encaminhe o paciente para a SALA BRANCA')

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
    resp = ''
    while resp != 'S' and resp != 'N':
        resp = str(input('Deseja cadastrar outro paciente? [S/N]')).upper().strip()[0]
print('ENCERRANDO...')