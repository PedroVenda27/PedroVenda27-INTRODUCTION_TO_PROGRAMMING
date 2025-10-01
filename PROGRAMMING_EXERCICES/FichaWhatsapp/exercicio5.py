# 5 Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

par = []
impar = []
todos = []

n=1
while n <= 20:
    numero = int(input(f"Insira o {n}º numero: "))
    if numero < 0:
        print("Insira um numero inteiro superior a 0")
    if numero > 0:
        if numero % 2 == 0:
            par.append(numero)
            todos.append(numero)
            n = n + 1
        if numero % 2 != 0:
            impar.append(numero)
            todos.append(numero)
            n = n + 1

print("LISTA DE PARES",par)
print("LISTA DE IMPARES",impar)