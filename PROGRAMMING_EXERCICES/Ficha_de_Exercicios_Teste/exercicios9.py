# 9) Escreva um programa em que o utilizador vai introduzindo
# números positivos até ser introduzido o valor 0 (zero). No fim o
#programa indicará a percentagem de números pares introduzidos.

trapp = 1
div2 = 0
x = 0
while trapp<=1:
    numero = int(input("Inroduza um número Positivo"))

    if numero % 2:
       div2 = div2 + 1
       x=x+1

    if numero < 0:
        print("Erro Pf insira um n positivo")
    
    elif numero == 0:
        trapp = 2

    else:
      x=x+1

percentagem = div2 / x * 100

print("Percentagem de numeros pares introduzidos = %.2f:", percentagem ,"%")

