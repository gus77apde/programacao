# Solicita ao usuário a velocidade média e a distância
velocidade_media = float(input("Digite a velocidade média (em km/h): "))
distancia = float(input("Digite a distância (em km): "))

# Calcula o tempo em horas
calculo = distancia/velocidade_media
horas= int(calculo)
minuto = int((calculo-horas)*60)

# Exibe o tempo em horas
print(f"O tempo necessário é de {horas} horas e {minuto} minutos")
