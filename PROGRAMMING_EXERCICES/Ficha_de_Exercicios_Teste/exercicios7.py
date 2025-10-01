# 7) Escreva um programa que leia 10 números inteiros introduzidos
# pelo utilizador e indique o máximo, a média, o mínimo e a soma
# dos valores.

Soma = 0
total = 0
minimo = 9999999
maximo = -999999



x=1
while x<=10:
    valorins = int(input("Insira o valor: "))
    x=x+1

    if valorins <= minimo:
       minimo = valorins

    if valorins >= maximo:
      maximo = valorins

    Soma=total+valorins
    total=Soma

print("minimo:",minimo)
print("maximo:",maximo)
print("Soma dos Valores:",Soma)
media= Soma / 10 
print("Média = %.2f:" % media)
