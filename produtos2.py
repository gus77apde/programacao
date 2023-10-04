import csv
def cadastrar_produto(produtos, produto, quantidade, valor):
    produto={
        'produto':produto,
        'quantidade':quantidade,
        'valor':valor
    }
    produtos.append(produto)
    print ("produto salvo no estoque")
produtos= []

def salvardados():
    with open ('produtos_csv', mode="w", newline="") as produto_csv:
        writer = csv.writer (produto_csv)
        writer.writerow(["nome", "quantidade", "valor"])
        for produto in produtos:
            writer.writerow([produto["produto"],produto["quantidade"],produto["valor"]])

print ("dados salvos com sucesso")
def ver_dados_csv():
    with open ('produtos_csv',mode='r') as produtos2_csv:
        dados_csv= csv.DictReader(produtos2_csv)
        for linha in dados_csv:
            print(f"nome: {linha['nome']},quantidade: {linha['quantidade']}, valor:{linha['valor']}")
while True:

    menu = float(input(
        "Escolha uma opção para o menu:\n"
        "1 - Inserir\n"
        "2 - imprimir\n"
    ))
    if menu==1:
        nome=(input("nome do produto"))
        quantidade=(input("quantidade"))
        valor=(input("valor"))
        cadastrar_produto (produtos,nome, quantidade,valor)
        salvardados()
    elif menu == 2:
        ver_dados_csv()