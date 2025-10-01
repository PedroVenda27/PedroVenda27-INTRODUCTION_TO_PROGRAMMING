# 5) Escreva um programa que peça ao utilizador um nome e um número
# inteiro (entre 1 e 20). Deverá mostrar esse nome um número de
# vezes igual a esse valor inteiro.



y=0

Nome = (input("Insira o Nome:"))

while y != 1:
    Numero = int(input("Insira o Numero de vezes a repetir o Nome (1-20):"))

    if Numero < 1 or Numero > 20:
        print("O número não está inserido entre os valores de 1 e 20")
    else:
        y = 1

if y==1:
    x = 1
    while x<=Numero:
        print (Nome)
        x=x+1