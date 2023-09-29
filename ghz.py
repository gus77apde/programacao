nomes = ["maca", "palmito", "banana", "uranio", "melancia",
         "cafe", "laxante", "quiabo", "pequi", "gilo"]
quantidades = [5, 3, 2, 7, 1, 4, 6, 2, 8, 10]
precos_unitarios = [100.0, 50.0, 75.0, 120.0, 200.0, 80.0, 60.0, 150.0, 90.0, 70.0]
imposto1 = 0.12
imposto2 = 0.06
imposto3 = 0.03
frete = 50.0
for i in range(len(nomes)):
    quantidade = quantidades[i]
    preco_unitario = precos_unitarios[i]
    preco_total_sem_impostos = quantidade * preco_unitario
    valor_imposto1 = preco_total_sem_impostos * imposto1
    valor_imposto2 = preco_total_sem_impostos * imposto2
    valor_imposto3 = preco_total_sem_impostos * imposto3
    preco_total_com_impostos = preco_total_sem_impostos + valor_imposto1 + valor_imposto2 + valor_imposto3 + frete
    print(f"Produto: {nomes[i]}")
    print(f"Quantidade: {quantidade}")
    print(f"Preço Unitário: R${preco_unitario:.2f}")
    print(f"Preço Total sem Impostos: R${preco_total_sem_impostos:.2f}")
    print(f"Imposto 1 (12%): R${valor_imposto1:.2f}")
    print(f"Imposto 2 (6%): R${valor_imposto2:.2f}")
    print(f"Imposto 3 (3%): R${valor_imposto3:.2f}")
    print(f"Frete: R${frete:.2f}")
    print(f"Preço de Venda com Impostos: R${preco_total_com_impostos:.2f}")
    print("\n")
total_geral = sum(quantidades[i] * precos_unitarios[i] for i in range(len(nomes))) + (len(nomes) * frete)
print(f"Total Geral (incluindo frete): R${total_geral}")
