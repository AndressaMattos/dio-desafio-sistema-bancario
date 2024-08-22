menu = """
Digite a operação desejada:

[D] Deposito
[S] Saque
[E] Extrato
[Q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    operacao = input(menu)
    operacao = operacao.upper()

    if operacao == "D":
        valor = float(input("Qual o valor de depósito?"))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print ({extrato})
        else: 
            print(f"Você falhou! O valor de depósiro R$ {valor:.2f} é inválido!")

    elif operacao == "S":
        valor = float(input("Informe o valor do Saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saques:
            print(f"Operação falhou! Número máximo de {LIMITE_SAQUES} saques excedidos)")
        
        elif excedeu_saldo:
            print(f"Operação falhou! O valor de saque (R$ {valor}) é maior que o saldo(R$ {saldo})")
        
        elif excedeu_limite:
            print(f"Operação falhou! O valor de saque (R$ {valor}) excede o limte(R$ {limite:.2f})")
        
        elif valor > 0:
            saldo -= valor
            extrato +=(f"Saque: R$ {valor:.2f}\n")
            numero_saques +=1       
        
        else:
            print(f"Operação falhou! O valor de saque (R$ {valor}) é inválido!")

    
    if operacao == "E":
        print(f"=====================EXTRATO=====================")
        print ("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print(f"=================================================")


    if operacao == "Q":
        print(f"Volte sempre!")
        break
