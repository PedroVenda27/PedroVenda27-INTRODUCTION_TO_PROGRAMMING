# 11) Escreva um programa que leia 10 números inteiros e indique se
# um número é igual ao anterior. No final deverá indicar quantos
# números introduzidos são iguais ao anterior.


contador = 0
numant = 0
x = 1

while x <= 10:
    numero = int(input("Digite um número inteiro: "))


    if numant == numero:
       contador = contador + 1
       print("O número inserido", numero, "é igual ao anterior")
       numant = numero
       x = x + 1


    if numant != numero:
        print("O número inserido", numero, "é diferente do anterior")
        numant = numero
        x = x + 1
   

print("Total de números iguais ao anterior:", contador)

