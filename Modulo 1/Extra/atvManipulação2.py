# 2. Agenda de Contatos
# Implemente um programa que crie e gerencie um arquivo chamado contatos.txt.
# Cada contato deve ter nome, telefone e e-mail.
# O programa deve:
# Permitir cadastrar novos contatos.
# Exibir todos os contatos cadastrados.
# OBS: Neste caso só iremos usar o os comandos de With , open e os modos de leitura
# e escrita da função open()

nome=input('Digite o seu nome: ')
telefone=input('Digite o seu telefone: ')
email=input('Digite o seu e-mail: ')

with open('Agenda de contatos','a') as arquivo:
   conteudo= arquivo.write(nome+ '|'+email+ '|'+ telefone+ '\n')


with open('Agenda de contatos','r') as arquivo:
  artur= arquivo.read()

  print(artur)