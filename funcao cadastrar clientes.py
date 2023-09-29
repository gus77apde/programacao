def cadastrar_cliente(clientes, nome, email, telefone):
    cliente={
        'nome': nome,
        'email':email,
        'telefone': telefone
    }
    clientes.append(cliente)
    print("cliente cadastrado com sucesso!")
def imprimir_clientes(clientes):
    for indice,cliente in enumerate (clientes):
        print(f"cliente {indice+1}")
        print(f"nome: {cliente['nome']}")
        print(f"nome: {cliente['email']}")
        print(f"nome: {cliente['telefone']}")
clientes= []

while True:
    print ("n\menu")
    print("1. cadastrar cliente")
    print("2. imprimir cliente")
    print("3. sair")
    opcao=int(input("digite uma opcao"))
    if opcao==1:
        nome=input("nome do cliente")
        email= input("email do cliente")
        telefone=input("telefone do cliente")
        cadastrar_cliente(clientes, nome, email, telefone)
    elif opcao==2:
        imprimir_clientes(clientes)
    elif opcao==3:
        print ("ate mais")
        break
    else:
        print("opcao invalida")

