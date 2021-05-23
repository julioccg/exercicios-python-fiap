nome = str(input('Nome: '))
idade = int(input('Idade: '))
if idade >= 65:
    print(f'O paciente {nome} \033[1;32mPOSSUI\033[m atendimento prioritário!')
else:
    print(f'O paciente {nome} \033[1;31mNÃO POSSUI\033[m atendimento prioritário!')
