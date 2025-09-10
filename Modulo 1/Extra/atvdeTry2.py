# Crie uma função chamada dividir(a, b) que retorne o resultado da divisão a / b.
# Utilize um bloco try-except genérico (sem especificar o tipo de exceção) para tratar
# quaisquer erros que possam ocorrer durante a operação (como divisão por zero ou tipos
# inválidos).
# Em caso de erro, a função deve retornar None.]


n=int(input('Digite um número para dividir:'))
n1=int(input('Digite outro número: '))

try:
    
    

    print(f'A divisão dos números é: {n / n1}')
except:
    print('none')