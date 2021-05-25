numero = int(input('Digite um numero para saber a tabuada: '))
for mult in range(1, 11, 1):
    print(f'\t{numero:3<} X {mult:3<}   =   {(numero * mult):3>}')