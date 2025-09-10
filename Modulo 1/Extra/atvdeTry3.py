# Peça ao usuário um índice e tente acessar um elemento em uma lista predefinida (ex: [10,
# 20, 30]). Use try-except para tratar IndexError (índice fora do intervalo) e ValueError (se o
# índice não for um inteiro). Exiba mensagens específicas para cada erro.


lista=[10,20,30]

try:
    print(lista[3])

except:

    li=input('Digite o número para lista: ')
    lista.append(li)

