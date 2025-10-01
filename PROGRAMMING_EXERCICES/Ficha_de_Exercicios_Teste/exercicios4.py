# 4) Crie um programa que escreva os números inteiros entre 0 e 100
# em intervalos (incremento) dados pelo utilizador. O intervalo
# deverá ser um número entre 1 e 10. (Por exemplo, com intervalos
# de 4).

y=0

while y != 1:
    intervalo = int(input("Insira o Intervalo"))

    if intervalo < 1 or intervalo > 10:
        print("O número não está inserido entre os valores de 1 e 10")
    else:
        y = 1

if y==1:
    x = 0
    while x<=100:
        if x % intervalo ==0 and x != 0:
            print (x)
        x=x+1

