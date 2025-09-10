a1=int(input('Digite a autonomia de km por litro: '))
a2=int(input('Digite os litros do tanque: '))


if a1 * a2 >= 450:
    print('Não precisa reabastecer')
else:
    print('Precisa reabastecer')