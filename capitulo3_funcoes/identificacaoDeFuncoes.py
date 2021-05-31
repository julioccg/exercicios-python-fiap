def preencherInventario(lista):
    resposta = 'S'
    while resposta == 'S':
        equipamento = [input("Equipamento: "), 
        float(input('Valor: ')), 
        int(input('Numero Serial: ')), 
        input('Departamento: ')]
        lista.append(equipamento)
        resposta = input('Digite \'S\' para continuar: ').upper()

def exibirInventario(lista):
    for elemento in lista:
        print(f'\nNome.............: {elemento[0]}')
        print(f'Valor............: {elemento[1]}')
        print(f'Serial...........: {elemento[2]}')
        print(f'Departamento.....: {elemento[3]}')

def localizarPorNome(lista):
    busca = input('\nDigite o nome do equipamento que deseja buscar: ')
    for elemento in lista:
        if busca == elemento[0]:
            print(f'Valor............: {elemento[1]}')
            print(f'Serial...........: {elemento[2]}')

def depreciarPorNome(lista, porc):
    depreciacao = input('\nDigite o nome do equipamento que será depreciado: ')
    for elemento in lista:
        if depreciacao == elemento[0]:
            print(f'Valor antigo: {elemento[1]}')
            elemento[1] = elemento[1] * (1 - porc / 100)
            print(f'Novo valor: {elemento[1]}')

def excluirPorSerial(lista):
    serial = int(input(f'\nDigite o serial do equipamento que será excluído: '))
    for elemento in lista:
        if elemento[2] == serial:
            lista.remove(elemento)
    return 'Itens excluídos.'

def resumirValores(lista):
    valores = []
    for elemento in lista:
        valores.append(elemento[1])
    if len(valores) > 0:
        print(f'O equipamento mais caro custa: {max(valores)}')
        print(f'O equipamento mais barato custa: {min(valores)}')
        print(f'O total de equipamentos é de: {sum(valores)}')