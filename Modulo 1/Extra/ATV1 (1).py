
lista=[-1, 2, 0,-5, -4, 3, -6]

positivos=0
negativo=0
zero=0



for lista in lista :
    if lista<0:
        negativo=negativo+1
    elif lista>0:
        positivos=positivos+1
    elif lista==0:
       
        zero=zero+1
       
 

print('Relatório:')
print ('negativo:',negativo)
print('positivos:', positivos)
print('zero:', zero)




