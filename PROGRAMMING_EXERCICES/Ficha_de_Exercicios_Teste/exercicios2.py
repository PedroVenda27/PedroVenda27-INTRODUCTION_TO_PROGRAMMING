# 2) Escreva um programa para imprimir todos os números inteiros
# entre dois valores introduzidos pelo utilizador. O programa deverá
# verificar qual dos dois valores é o maior.



maior=0
menor=0

Valor1 = int(input("Insira o Valor 1: "))
Valor2 = int(input("Insira o Valor 2: "))

if Valor1==Valor2:
    maior = Valor1 = Valor2
    menor = Valor1 = Valor2

elif Valor1 > Valor2:
    maior = Valor1
    menor = Valor2

else:
    maior = Valor2
    menor = Valor1
    

x=menor
while x<=maior:
    print (x)
    x=x+1