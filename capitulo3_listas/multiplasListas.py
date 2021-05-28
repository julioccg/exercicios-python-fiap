equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = 'S'
while resposta == 'S':
    equipamentos.append(input('Equipamento: '))
    valores.append(float(input('Valor: ')))
    seriais.append(int(input('Número Serial: ')))
    departamentos.append(input('Departamento: '))
    resposta = input('Digite \'S\' para continuar: ').upper()
for indice in range(0, len(equipamentos)):
    print(f'\nEquipamento...: {indice + 1}')
    print(f'Nome..........: {equipamentos[indice]}')
    print(f'Valor.........: {valores[indice]}')
    print(f'Serial........: {seriais[indice]}')
    print(f'Departamento..: {departamentos[indice]}')

busca = input(f'\nDigite o nome do equipamento que deseja buscar: ')
for indice in range(0, len(equipamentos)):
    if busca == equipamentos[indice]:
        print(f'Valor...: {valores[indice]}')
        print(f'Serial..: {seriais[indice]}')

depreciacao = input('\nDigite o nome do equipamento que será depreciado: ')
for indice in range(0, len(equipamentos)):
    if depreciacao == equipamentos[indice]:
        print(f'Valor antigo: {valores[indice]}')
        valores[indice] = valores[indice] * 0.9
        print(f'Novo valor: {valores[indice]}')

serial = int(input('\nDigite o serial do equipamento que será excluído: '))
for indice in range(0, len(equipamentos)):
    if seriais[indice] == serial:
        del departamentos[indice]
        del equipamentos[indice]
        del seriais[indice]
        del valores[indice]
        break

for indice in range(0, len(equipamentos)):
    print(f'\nEquipamento...: {indice + 1}')
    print(f'Nome..........: {equipamentos[indice]}')
    print(f'Valor.........: {valores[indice]}')
    print(f'Serial........: {seriais[indice]}')
    print(f'Departamento..: {departamentos[indice]}')