saldo = 0.0 #Variavel que guardará o saldo do usuário
while True:    
    #Cadastro de usuario e senha
    #Menu Principal
    #Ler a escolha do usuario
    escolha_menu = int(input("Bem Vindo ao menu!! \n1. Cadastrar\n2. Login\n3. Encerar\nSelecione: "))
    #Se o usuario escolher cadastro
    if escolha_menu == 1:
        usuario = input("\nCrie um nome de usuário: ")
        senha = input("\nCrie uma senha: ")  
    elif escolha_menu == 2: #Se o usuario escolher login
        #Comparar as inf. cadastradas com uma leituras
        login_usuario = input("\nDigite seu usuario: ")
        login_senha = input("\nDigite sua senha: ")
        if login_usuario == usuario and login_senha == senha:
            print("\nLOGIN REALIZADO COM SUCESSO.")
            #Se o login correto, entra no menu principal do app
            print("Bem Vindo:", usuario)
            while True:
                escolha_principal = int(input("\n1. Depósito\n2. Sacar\n3. Pix\n4. Extrato\n5. Encerar\nSelecione: "))
                if escolha_principal == 1:
                    valor_deposito = float(input("Digite o valor do depósito: "))
                    saldo += valor_deposito
                    print("O novo saldo é:", saldo)
                elif escolha_principal == 2:
                    valor_saque = float(input("Digite o valor do saque: "))
                    senha_saque = input("Digite sua senha: ")
                    if senha_saque == senha:
                        saldo -= valor_saque
                    else:
                        print("Senha incorreta.")
                elif escolha_principal == 3:
                    valor_pix = float(input("Digite o valor do pix: "))
                    senha_pix = input("Digite sua senha: ")
                    if senha_pix == senha:
                        saldo -= valor_pix
                    else:
                        print("Senha incorreta: ")
                elif escolha_principal == 4:
                    senha_extrato = input("Digite sua senha: ")
                    if senha_extrato == senha:
                        print("Extrato", saldo)
                    else:
                        print("Senha incorreta")
                elif escolha_principal == 5:
                    senha_encerramento = input("Digite sua senha: ")
                    if senha_encerramento == senha:
                        break
                    else:
                        print("Senha incorreta.")
        else:
            print("\nUSUÁRIO OU SENHA INCORRETOS.")
    else:
        break