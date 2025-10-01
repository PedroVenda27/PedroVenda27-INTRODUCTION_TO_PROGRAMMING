#24) Crie um programa para escrever a série de Fibonacci até a um
#limite pedido pelo utilizador. (0, 1, 2, 3, 5, 8, 13, 21...)


limite = int(input("Introduza o limite até o qual deseja fazer a série de Fibonacci: "))

a = 1
b = 2

while a <= limite:
    print(a)
    a, b = b, a + b