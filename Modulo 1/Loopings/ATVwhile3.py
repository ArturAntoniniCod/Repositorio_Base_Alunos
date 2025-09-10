numero=int(input('Digite um número de 10 a 0: '))

while numero<0 or numero>10:
    print('Número errado')

    numero=int(input('digite novamente: '))

    
print('O numero está correto.')