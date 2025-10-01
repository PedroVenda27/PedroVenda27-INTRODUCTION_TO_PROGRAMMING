# 3) Escreva um programa que apresente a tabuada dum número inteiro
# entre 1 e 9 dado pelo utilizador. Se o número estiver fora dessa
# gama, o programa deverá dar uma mensagem.

y = 0

while y != 1:
    tabuada = int(input("Insira o Numero Referente a Tabuada (1-9): "))

    if tabuada < 1 or tabuada > 9:
        print("O número não está inserido entre os valores de 1 e 9")
    else:
        y = 1

if y == 1:
    x = 0
    while x <= 10:
        print(tabuada, "x", x, "=", tabuada * x)
        x = x + 1