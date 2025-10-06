# Usando sua API Crie um sistema que exclua todos os pedidos que tenha
# Pizza (Eu odeio pizza 😝)
# Você vai usar o método GET para trazer as informações , o método delete para
# dele deletar
# OBS: você terá que usar o for para conseguir puxar o id e o pedido e if e else para
# saber se esse pedido é igual a pizza ou não.


import requests

dados= requests.get('https://68dea902898434f41355972e.mockapi.io/Restaurante')

result= dados.json()

for i in result:
   id=i.get('id')
    
for i in result:
    prato=i.get('Prato')

    if prato=='pizza':
    
        requests.delete(f'https://68dea902898434f41355972e.mockapi.io/Restaurante/{id}')
    else:
        print('Peça outra coisa')
   


    

