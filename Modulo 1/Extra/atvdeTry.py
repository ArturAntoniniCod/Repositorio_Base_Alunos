# Escreva um programa que solicite um número inteiro ao usuário. Use try-except para tratar
# entradas não numéricas e valores não inteiros. Se ocorrer um erro, peça a entrada
# novamente até que seja válida.

n=input('Digite um número: ')

try:
    n=int(n)

    print('válido')
except:
    print('Digite um número correto')