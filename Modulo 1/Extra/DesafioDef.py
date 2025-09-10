

nu=int(input('Digite algum número para saber a sua classificação: '))

def numero(nu):
    if nu<0:
        print("Número negativo")
    elif nu>=0 and nu<=10:
        print("Entre 0 e 10")
    elif nu>=10 and nu<=100:
        print("Entre 10 e 100")
    elif nu>100:
        print("Maior que 100")

numero(nu)