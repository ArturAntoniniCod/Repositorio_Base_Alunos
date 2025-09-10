# Esta atividade vai trabalhar os comandos Try except e também o comando open()
# para criação do arquivo o intuito é tentar realizar a leitura do arquivo caso ele não
# exista você deve tratar este erro criando o arquivo.
# Passo a passo:
# Usando os conceitos de Try e Except tente fazer a leitura de um arquivo usando o
# comando.
# with open('nome do arquivo', 'modo') as arquivo:
# variavel = arquivo.modo('conteudo que voce quer inserir')
# print(variavel)
# agora é com você , de forma criativa trate o erro usando Except
# OBS: as palavras variável ,modo e nome do arquivo devem ser substituídas 😉


nome= input('Digite o nome: ')
email= input('Digite o e-mail')

try:
   with open('Atividade Manipulação de arquivo','r') as arquivo:
      ar=arquivo.read()

except:
     with open('Atividade Manipulação de arquivo','a') as arquivo:
       arquivo.write(nome+ '|' + email + '\n')
