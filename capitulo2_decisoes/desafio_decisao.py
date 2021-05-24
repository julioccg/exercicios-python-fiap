print('\033[1;30;47m-=' * 20)
print('{:^40}'.format('SISTEMA'))
print('-=' * 20, '\033[m')
nivelAcesso = str(input('Digite seu nível de acesso: [ADM][USR][GUEST] ')).upper().strip()
genero = str(input('Digite M ou F: ')).upper().strip()[0]
if genero == 'M':
    if nivelAcesso == 'ADM':
        print('Bem vindo ADMINISTRADOR!')
    elif nivelAcesso == 'USR':
        print('Bem vindo USUÁRIO!')
    elif nivelAcesso == 'GUEST':
        print('Bem vindo VISITANTE!')
    else:
        print('OLÁ DESCONHECIDO')
else:
    if nivelAcesso == 'ADM':
        print('Bem vindo ADMINISTRADORA!')
    elif nivelAcesso == 'USR':
        print('Bem vindo USUÁRIA!')
    elif nivelAcesso == 'GUEST':
        print('Bem vindo VISITANTE!')
    else:
        print('OLÁ DESCONHECIDA')
