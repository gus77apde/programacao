# Solicitar a população e a taxa de crescimento do primeiro país
populacao_pais1 = float(input("Insira a população inicial do primeiro país: "))
taxa_crescimento_pais1 = float(input("Insira a taxa de crescimento anual do primeiro país (em decimal): "))

# Solicitar a população e a taxa de crescimento do segundo país
populacao_pais2 = float(input("Insira a população inicial do segundo país: "))
taxa_crescimento_pais2 = float(input("Insira a taxa de crescimento anual do segundo país (em decimal): "))

# Verificar se o primeiro país já tem uma população maior que o segundo país
if populacao_pais1 >= populacao_pais2:
    print("O primeiro país já tem uma população igual ou maior que o segundo país.")
else:
    # Inicializar o número de anos como zero
    anos = 0

    # Calcular o número de anos necessários em um loop
    while populacao_pais1 < populacao_pais2:
        populacao_pais1 *= (1 + taxa_crescimento_pais1)
        anos += 1

    print(f"O primeiro país levará cerca de {anos} anos para alcançar a população do segundo país.")
