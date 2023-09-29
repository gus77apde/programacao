produto=[]
valor=[]
quantidade=[]
frete=[]
porcvenda=[]
while True:
    menu= float (input(
        "1 - inserir produto\n"
        "2- meus produtos\n"
    
    ))
    
    if menu ==1:
        
         #primeira funçao pra inserir produto
         produtos= (input("digite seu produto:" ))
         valores= int(input ("digite o valor:" ))
         quantidades= int(input("digite a quantidade:" ))
         fretes= int(input("digite o valor do frete:" ))
         porcentagem= (input("porcentagem de venda:" ))
         produto.append(produtos)
         valor.append(valores)
         quantidade.append(quantidades)
         frete.append(fretes)
         porcvenda.append(porcentagem)
         print (f"produto inserido com sucesso")
         print( )
    # segunda funcao atualizar os produto
    
    elif menu ==2:
         for i in range(len(produto)):
            quantidades=quantidade[i]
            valores= valor[i]
            fret= frete[i]
            umimposto= valores * 0.12
            doisimposto=valores*0.06
            tresimposto= valores*0.03
            fretii= quantidades/fret
            precototal= valores+umimposto+doisimposto+tresimposto+fretii
         for i in range(len(produto)):
              print(f"{produto[i]}, {precototal:.2f}")