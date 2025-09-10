nome=input('Digite o seu nome: ')
horario=input('Digite um horário(manhã,tarde ou noite):')

def escreve(nome, horario):
    if horario=='manhã':
        print('Olá',nome,',Bom dia!')
    elif horario=='tarde':
        print('Olá',nome,',Boa tarde!')
    elif horario=='noite':
        print('Olá',nome,',Boa noite!')

escreve()