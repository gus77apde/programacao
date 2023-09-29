horas= float(input("Digite quanto ganha por hora:\n"))
ganhoph= float(input("horas trabalhadas:\n"))
salario= horas * ganhoph
ir= salario* 0.11
print ("imposto sobre renda:", ir, "reais")
inss= salario *0.08
print("inss:", inss, "reais")
sindicato= salario * 0.05
print("contribuiçao com o sindicato:", sindicato, "reais")
salarioliquido= salario-ir-inss-sindicato
print("seu salario é de",salarioliquido, "reais")
