print('Caixa eletronico:\n(1)Sacar\n(2)Depositar\n(3)Ver Saldo\n(4)Sair')
total=1000
while True:
    option=input('digite a opção:')

    if option=='1':
        saque=int(input('Valor de saque:'))
   
        if saque>total:
         print('não tem amigao')
        else:
            total=total-saque
            print(total,'Saque realizado com sucesso')

    elif option=='2':
        deposit=int(input('Valor de deposito: '))
        total= total+deposit
        print('Este é o total: ',total)
   
    elif option =='3':
        
        print('ver saldo',total)
    elif option=='4':
        print('Obrigado por usar nossos serviços!')
        break