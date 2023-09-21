metros=int (input("quantos metros quadrados"))
preco=80.00
lata= 18
calc=metros * 0.33
if calc <=18:
    print ("vai utilizar",calc,"litros", preco, "reais")
if calc >18 <35.99:
    print("vai utilizar",calc,"litros de tinta", preco*2, "reais")
if calc >36<54:
    print ("vai utilizar", calc,"litros", preco*3,"reais")
if calc >54<72:
    print ("vai utilizar",calc,"litros", preco*4, "reais")
