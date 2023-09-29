tamanho=int(input("digite o tamanho do arquivo em mb: "))
velocidade= int(input("velocidade da sua internet em mb:"))
resultado= tamanho/(velocidade/8)
if resultado<= 1:
    print(resultado, "centesimos")
if resultado >1<60:
    print(resultado, "segundos")
if resultado >60<3600:
    print (resultado/60, "minutos")
if resultado >3600<86400:
    print (resultado/3600, "horas")
if resultado >86400:
    print(resultado/86400, "dias")