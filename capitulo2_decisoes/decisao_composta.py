nome = str(input('Nome: '))
idade = int(input('Idade: '))
doenca_infectocontagiosa = input('Suspeita de doença infecto-contagiosa? [S/N] ').upper().strip()[0]
if idade >= 65 and doenca_infectocontagiosa =='S':
    print(f'O paciente {nome} será direcionado para \033[1;30;43mSALA AMARELA\033[m - \033[1;31mCOM PRIORIDADE!\033[m')
elif idade < 65 and doenca_infectocontagiosa =='S':
    print(f'O paciente {nome} será direcionado para \033[1;30;43mSALA AMARELA\033[m - \033[1;31mSEM PRIORIDADE!\033[m')
elif idade >= 65 and doenca_infectocontagiosa =='N':
    print(f'O paciente {nome} será direcionado para \033[1;30;47mSALA BRANCA\033[m - \033[1;31mCOM PRIORIDADE!\033[m')
elif idade < 65 and doenca_infectocontagiosa =='N':
    print(f'O paciente {nome} será direcionado para \033[1;30;47mSALA BRANCA\033[m - \033[1;31mSEM PRIORIDADE!\033[m')
else:
    print(f'Responda com SIM OU NÃO!')
