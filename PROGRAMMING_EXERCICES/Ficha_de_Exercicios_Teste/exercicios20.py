# 20) Escreva um programa em que o utilizador introduza números até
# introduzir um número par seguido de um número ímpar.

a = 0

while a == 0:
    numero = int(input("Introduza um número: "))
    if numero % 2 == 0:
        a = 1
    else: 
        a = 0

while a == 1:
    numero = int(input("Introduza um número: "))
    if numero % 2 != 0:
        a = 2
    else: 
        a = 1