import requests

print('Digite:\n(1)para pedir\n(2)para mudar o pedido\n(3)para removar\n(4)sair')

while True:
     dados= requests.get('https://68dea902898434f41355972e.mockapi.io/Restaurante').json()
     option=input('Digite a opção desejada:')
     if option=='1':
         prato= input('Qual prato você quer comer? ')
         bebida=input('Qual a bebida que vc deseja tomar? ')
         mesa= input('Qual a sua mesa?')
         pedido={   
            'Prato': prato,
            "Bebidas": bebida,
            "mesa": mesa,     
                }
         requests.post('https://68dea902898434f41355972e.mockapi.io/Restaurante',pedido)
         print('Seu pedido foi enviado para cozinha!')

     elif option=='2':
        for i in dados:
         id=print(i.get('id'))

        print('Vi que você errou, insira novamente o que você deseja:')
        prato= input('Qual prato você quer comer? ')
        bebida=input('Qual a bebida que vc deseja tomar? ')
        mesa= input('Qual a sua mesa? ')
        id1=input('Qual o seu ID ')
        pedido={   
                'Prato': prato,
                "Bebidas": bebida,
                "mesa": mesa,
            }
        requests.put(f'https://68dea902898434f41355972e.mockapi.io/Restaurante/{id1}',pedido) 
        print('Seu pedido foi reenviado para a cozinha')
        
     elif option=='3':
         for i in dados:
            id=print(i.get('id'))
         id1=input('Qual o seu ID ')
         print('Seu pedido sera deletado')
         requests.delete(f'https://68dea902898434f41355972e.mockapi.io/Restaurante/{id1}')
     
     if option=='4':
         print('Volte e mande o seu feedback')
         break                 
            
