print('-' * 60)                 #Fazendo uma linha
print(f'\033[1;33m{"VARIAVEIS":^60}\033[m')     #Centralizado em 60 caracteres e trabalhando com cores
print('-' * 60)                 #Fazendo uma linha
nome = str(input('Digite o nome de um funcionário: '))
empresa = str(input('Digite a instituição: '))
qtde_funcionarios = int(input('Digite a quantidade de funcionários: '))
mediaMensalidade = float(input('Digite a média da mensalidade: '))
print()
print('=' * 60)
print(f'{nome} trabalha na empresa {empresa}')
#print('{} trabalha na empresa {}'.format(nome, empresa))
print(f'Possui: {qtde_funcionarios} funcionarios.')
print(f'A média da mensalidade é de: R$ {mediaMensalidade}.\n')
print('\033[1;36;47m{:=^60}\033[m'.format('VERIFIQUE OS TIPOS DE DADOS ABAIXO: '))     #Centralizado em 60 carac e preenchimento c =
print(f'O tipo de dado da variável [nome] é: \033[1;41m{type(nome)}.\033[m')
print(f'O tipo de dado da variável [empresa] é \033[1;41m{type(empresa)}.\033[m')
print(f'O tipo de dado da variável [qtde_funcionarios] é \033[1;41m{type(qtde_funcionarios)}.\033[m')
print(f'O tipo de dado da variável [mediaMensalidade] é \033[1;41m{type(mediaMensalidade)}.\033[m')
