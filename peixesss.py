peixe=[]
valor=[]
while True:
    menu= float (input(
        "1 - inserir produto\n"
        "2- meus produtos\n"
    
    ))
    
    if menu ==1:
        
         #primeira funçao pra inserir produto
         produtos= (input("digite seu produto:" ))
         valores= int(input ("digite o valor:" ))
         peixe.append(produtos)
         valor.append(valores)
         print (f"produto inserido com sucesso")
    # segunda funcao atualizar os produto
    
    elif menu ==2:
         for i in range(len(peixe)):
            peixes=peixe[i]
            valores=valor[i]
            
         for i in range(len(peixe)):
              print(f"{peixe[i]}, {valores:.2f}")