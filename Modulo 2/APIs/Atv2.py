# 2. Um bebê colocou fogo na mesa 5 😮 pegue todos os pedidos feitos na mesa 5 e
# delete porém a família não desistiu do jantar você terá que passar todos os pedidos
# feitos na mesa 5 e passar para a mesa 6.
# Você vai usar GET, DELETE e POST e também vai usar if e for.
# OBS: Se atente a ordem primeiro você vai fazer um post depois você vai deletar os
# pedidos da mesa

import requests

dados=requests.get('https://68dea902898434f41355972e.mockapi.io/Restaurante').json()



for i in dados:
    id=i.get('id')
    mesa=i.get('mesa')


    if '5' in mesa:
        pedido={   
    'Prato': i.get('Prato'),
    "Sobremesa": i.get('sobremesa'),
    "mesa": '6',
    "Bebidas": i.get('bebida'),
        }

        pedido=requests.post('https://68dea902898434f41355972e.mockapi.io/Restaurante',pedido)

        requests.delete(f'https://68dea902898434f41355972e.mockapi.io/Restaurante/{id}')
    
    
     

 




