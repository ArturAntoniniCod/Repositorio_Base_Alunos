n= int(input('Qual o preço do produto: '))

if n>= 100:
    print(n*10/100,'Este é o valor descontado do seu produto.')
elif n < 100:
    print('Você não tem nenhum desconto.')