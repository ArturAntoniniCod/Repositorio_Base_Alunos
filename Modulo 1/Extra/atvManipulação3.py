
# 3 Crie um sistema que regista o nome e 3 notas do aluno depois você vai validar se a média
# do aluno é maior que 7 caso seja maior você deve registrar em um documento o nome dele
# e se ele está aprovado ou reprovado.O sistema deve estar em um loop e deve ser
# encerrado somente se o usuário digitar a opção 0
# OBS: Esse é difícil ❤️

while True:
  option= input('Digite 1 para validar a média do aluno ou 0 para sair: ')
  
    
  if option=='1':
        nome=input('Digite o seu nome: ')
        nota=int(input('Digite a sua nota: '))
        nota1=int(input('Digite a sua nota: '))
        nota2=int(input('Digite a sua nota: '))
   
        resultado= (nota+nota1+nota2)/3
        if resultado>=7:
            with open('Boletim','a') as arquivo:
                arquivo.write(str(resultado))
                print('Você está aprovado')       
        else:
            with open('Boletim','a') as arquivo:
                arquivo.write(str(resultado))
                print('Você está reprovado')  
  elif option =='0':
        
        break; 