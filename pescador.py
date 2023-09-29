
peso=float(input("digite a quantidade pescada:\n"))
multa=4
caranha=7.5
valor=peso*caranha
if peso>50:
    var= peso-50
    print ("ira receber uma multa de", var * multa,"pagara no total dos peixes", valor+ (var*multa), "reais")
else:
    print ("nao pagará multa", "preco total pescado", valor,"reais")
