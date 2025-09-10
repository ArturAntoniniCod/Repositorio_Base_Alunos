print('(1) Adicionar unidades ao estoque\n(2) Remover unidades do estoque\n(3) Verificar estoque atual\n(4) Sair')
total=50
while True:
    op=input('Digite uma das opções: ')
    if op=='1':
        saque=int(input('Adicione unidades no estoque:'))
        total=total+saque
        print('O valor foi adicionado ao estoque.')
    elif op=='2':
        unidades=int(input('Quantas unidades você deseja remover: '))
        if unidades>total:
            print('Não tem amigão.')
        else:
            total=total-unidades
            print('As unidades foram removidas do estoque')
    elif op=='3':
        print('Este é o seu estoque:',total)
    elif op=='4':
        print('Obrigado por usar os nossos serviços')
        break

        

        


