# 23) Escreva um programa que indique ao utilizador todos os números
# primos entre dois números inteiros introduzidos pelo utilizador.


maximo = 0
minimo = 0
trapp = 1 

while trapp == 1:
    numero1 = int(input("Introduza o primeiro número: "))
    numero2 = int(input("Introduza o segundo número: "))


    if numero1 > numero2:
        maximo = numero1
        minimo = numero2
        trapp = 2

    if numero2 > numero1:
        maximo = numero2
        minimo = numero1
        trapp = 2
    
    else:
        print("Os numeros introduzidos sao iguais por favor insira numros difrentes entre eles")
        trapp = 1


while trapp == 2:

    for numeroatual in range(minimo,maximo + 1):
        primo = 1
        if numeroatual <= 1:
            primo = 0
        else:
            # Verifica se o número é primo
            for i in range(2, numeroatual):
                if numeroatual % i == 0:
                    primo = 0
                    break
            if primo == 1: 
                print("O número", numeroatual, "é primo.")

    trapp=3
               
                    
        