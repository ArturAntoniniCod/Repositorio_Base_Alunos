
n1=int(input('Digite um número:'))
n2=int(input('Digite outro número: '))
escolha=input('Quer soma, multiplicar, subtrair ou dividir? ')


def somas (n1,n2,escolha):
    if escolha=='soma':
        print(n1+n2)
    elif escolha=='subtrair':
        print(n1-n2)
    elif escolha=='multiplicar':
        print(n1*n2)
    elif escolha== 'dividir':
        print(n1/n2)


somas(n1,n2,escolha)