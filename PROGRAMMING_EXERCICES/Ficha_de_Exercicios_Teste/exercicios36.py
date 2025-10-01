# 36) Sequência de Padovan: Similar à sequência de Fibonacci, a
# sequência de Padovan é definida da seguinte forma: P(n) = P(n-2) +
# P(n-3) com os primeiros valores P(0) = 1, P(1) = 1, P(2) = 1.
# Escreva um programa que mostre os primeiros n termos 


limite = int(input("Introduza o limite até o qual deseja fazer a série de Fibonacci: "))
x = 1
a = 1
b = 1
c = 1

while x <= limite:
    d = a+b
    print(d)
    a = b
    b = c
    c = d
    x=x+1