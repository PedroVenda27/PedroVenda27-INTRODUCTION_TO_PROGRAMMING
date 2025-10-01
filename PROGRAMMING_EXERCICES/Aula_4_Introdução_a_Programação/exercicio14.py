

print("Insira os dia mês e ano da 1ª data")
dia1= (input("Dia:"))
mes1 = (input("Mês"))
ano1 = (input("Ano:"))

print("Insira os dia mês e ano da 2ª data")
dia2= (input("Dia:"))
mes2 = (input("Mês"))
ano2 = (input("Ano:"))

if ano1 > ano2:
    print("A Primeira data é a mais recente")
elif ano2 > ano1:
    print("A Segunda data é a mais recente")
elif ano1 == ano2 and mes1 > mes2:
    print("A Primeira data é a mais recente")
elif ano1 == ano2 and mes2 > mes1:
    print("A Segunda data é a mais recente")
elif ano1 == ano2 and mes2 == mes1 and dia1 > dia2:
    print("A Primeira data é a mais recente")
elif ano1 == ano2 and mes2 == mes1 and dia2 > dia1:
    print("A Segunda data é a mais recente")
else:
    print("As datas são iguais")
