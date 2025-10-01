# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. 
# Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, 
# e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

n = 1
temperaturas = []
mes_acima_da_media = []


while n <= 12:
        temperatura = int(input(f" Insira a temperatura referente ao mes {n}: "))
        if temperatura <= -20  or  temperatura >= 50 :
            print("insira valores validos valido")
        else:
            temperaturas.append(temperatura)
            n = n + 1

media_temperaturas = sum(temperaturas) / 12

for i , temp in enumerate(temperaturas):
     if temp > media_temperaturas:
          mes_acima_da_media.append(i)

print("Meses Acima da Média")
for num in mes_acima_da_media:
     if num == 0:
          print("Janeiro")
     if num == 1:
          print("Fevereiro")
     if num == 2:
          print("Março")
     if num == 3:
          print("Abril")
     if num == 4:
          print("Maio")
     if num == 5:
          print("Junho")
     if num == 6:
          print("Julho")
     if num == 7:
          print("Agosto")
     if num == 8:
          print("Setembro")
     if num == 9:
          print("Outubro")
     if num == 10:
          print("Novembro")
     if num == 11:
          print("Dezembro")