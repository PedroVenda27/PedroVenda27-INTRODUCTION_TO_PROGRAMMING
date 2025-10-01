# 13) [utilização de flags (ou não…)]. Escreva um programa que leia
# n números (sendo n introduzido pelo utilizador) e indique se os
# números são todos pares, se são todos ímpares ou se há ambos os
# tipos.


par = 0
impar = 0

n = int(input("Introduza o número de classificações a inserir: "))
x = 1

while x <= n:
    numero = int(input("Introduza um número: "))

    if numero % 2 == 0:
        # PAR
        par = par + 1
    else:
        # IMPAR
        impar = impar + 1

    x = x + 1

if par > 0 and impar == 0:
    print("Apenas foram inseridos números pares.")
elif par == 0 and impar > 0:
    print("Apenas foram inseridos números ímpares.")
else:
    print("Foram inseridos números pares e ímpares.")