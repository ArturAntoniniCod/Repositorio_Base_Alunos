idade=int(input('Digite a sua idade: '))
classe=input('Você é estudante(sim/não)? ')

if classe =='não'and idade >=13 and idade <=64:
     print('O valor do ingresso é de 20 reais.')
elif classe == 'sim' and idade >0 and idade <100:
     print('O valor do ingresso é de 12 reais.')
elif classe == 'não' and idade >65 and idade <100:
     print('O valor é de 10 reais.')
elif classe == 'não' and idade >0 and idade <12:
     print('O valor do ingresso é de 8 reais')

  