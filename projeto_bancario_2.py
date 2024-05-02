import sys

menu = ( '''
========== SELECIONE UMA OPÇÃO ==========
 [1] Depositar;
 [2] Sacar;
 [3] Extrato;
 [0] Sair.
=========================================             
=>''' )

saldo = 0
limite_saque = 500
extrato = ""
numero_saques = 0
SAQUE_POR_DIA = 3

while True:

    opcao = int(input(menu))

    if opcao == 1:
        deposito = float( input( "Informe o valor do deposito: R$" ) )

        if deposito > 0:
            saldo += deposito
            extrato += f" Deposito: R${deposito:.2f} realizado com sucesso! \n "

        else:
            print( "Desposito negado! O valor informado é inválido." )

    elif opcao == 2:
        saque = float( input( "Informe o valor do saque: R$" ) )

        excedeu_saldo = saque > saldo

        excedeu_limite = saque > limite_saque

        excedeu_saques = numero_saques >= SAQUE_POR_DIA
        
        if excedeu_saldo:
            print( "Saque negado! Seu saldo não é suficiente!" )
        
        elif excedeu_limite:
            print( "Saque negado! O valor do saque excede o limite permitido." )

        elif excedeu_saques:
            print( "Saque negado! Excedeu o número máximo de saques diários." )

        elif saque > 0:
            saldo -= saque
            extrato += f" Saque: R${saque:.2f} realizado com sucesso! \n "
            numero_saques += 1

        else:
            print(" Valor do saque é inválido ")
    
    elif opcao == 3:
        print( "\n >>>>>>>>>>>>>>> EXTRATO <<<<<<<<<<<<<<< " )
        print( "Não foram realizadas movimentações." if not extrato else extrato )
        print( f"\n Saldo: R${saldo:.2f}" )
        print( ">>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<" )
    
    elif opcao == 0:
        print( "Agradeçemos a preferência!\n Saindo do sistema..." )
        break

    else:
        print( "Opção inválida! Selecione novamente outra opção!" )