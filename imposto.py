produto= ["mercurio", "uranio", "arsenio", "chumbo", "cadmio","cromo", "niquel", "cianeto", "plutonio", "magnesio"]
quantidade=[5,6,10,20,12,7,9,15,9,12]
preco=[15,40,12,6,12,40,32,7,5,10]
imposu=0.12
imposd=0.06
impost=0.03
frete=50
for i in range(len(produto)):
    quantidades=quantidade[i]
    precos= preco[i]
    umimposto= precos * imposu
    print(umimposto)
    doisimposto=precos*imposd
    tresimposto= precos*impost
    fretes= quantidades/frete
    precototal= precos+umimposto+doisimposto+tresimposto+fretes
    print(f"Produto: {produto[i]}")
    print(f"Quantidade: {quantidades}")
    print(f"Preço : R${precos}")
    print(f"Imposto 1 (12%): R${imposu}")
    print(f"Imposto 2 (6%): R${imposd}")
    print(f"Imposto 3 (3%): R${impost}")
    print(f"Frete: R${frete}")
    print(f"Preço de Venda com Impostos: R${precototal}")
    print(f"Preço de Venda com Impostos: R${precototal+precototal*0.60}")
    print("\n")

