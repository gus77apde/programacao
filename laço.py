# 3 numeros comando "for" "range" 
numa=int (input("comecar com  "))
numb=int (input("parar "))

for b in range(numa, numb):
    if b % 2 == 0:
        print ("par",b)
    else:
        print ("impar",b)