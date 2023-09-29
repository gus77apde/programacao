def cadastrar_produto(produtos, nome, quantidade, valor):
    produto={
        'nome':nome,
        'quantidade':quantidade,
        'valor':valor
    }
    produtos.append(produto)
    print ("produto salvo no estoque")
def mostrar_produtos (produtos):
    for indice,produto in enumerate (produtos):
        print(f"produto{indice+1}")
        print(f"nome: {produto['nome']}")
        print(f"quantidade: {produto['quantidade']}")
        print(f"valor: {produto['valor']}")
produtos= []
while True:
    print ("n\O que deseja?")
    print ("1:  cadastrar produto")
    print ("2:  Mostrar produtos cadastrados")
    print ("3:  voltar a tela inicial")
    opcao= int(input("digite uma opcao valida:\n"))
    if opcao==1:
        nome= input("produto desejado: \n")
        quantidade= int(input("Quantas unidades voce tem?: \n"))
        valor= float(input("valor do produto: \n"))
        cadastrar_produto(produtos,nome,quantidade,valor)
    elif opcao ==2:
        mostrar_produtos(produtos)
    elif opcao ==3:
        print ("té logo maraba")
        break
    else:
        print("opçao nao indentificada, por favor selecione uma das opções: ")