n = input('Digite alguma palavra: ')
vogais = 'aeiou'
contador = 0 

print('Essas são as vogais:')
for i in n:
    if i in vogais:
        print(i)
        contador += 1

print(f'Total de vogais: {contador}')