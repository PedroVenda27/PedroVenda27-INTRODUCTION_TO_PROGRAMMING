# 14) Escreva um programa que apresente todos os números inteiros
# entre dois números float introduzidos pelo utilizador.

trapp = 1

numero1 = float(input("Insira um 1º Numero: "))
numero2 = float(input("Insira um 2º numero: "))

if numero1 > numero2:
    maior = numero1
    menor = numero2

if numero2 > numero1:
    maior = numero2
    menor = numero1

while menor <= maior:
    print(int(menor))
    menor=menor+1

