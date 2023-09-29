# Dados do primeiro país
populacao_pais1 = 80000
taxa_crescimento_pais1 = 0.03

# Dados do segundo país
populacao_pais2 = 200000
taxa_crescimento_pais2 = 0.015

# Inicializar o número de anos como zero
anos = 0

# Enquanto a população do primeiro país for menor que a do segundo país
while populacao_pais1 < populacao_pais2:
    # Aplicar o crescimento populacional anual a ambos os países
    populacao_pais1 *= (1 + taxa_crescimento_pais1)
    populacao_pais2 *= (1 + taxa_crescimento_pais2)
    anos += 1

print(f"O primeiro país levará cerca de {anos} anos para alcançar a população do segundo país.")
