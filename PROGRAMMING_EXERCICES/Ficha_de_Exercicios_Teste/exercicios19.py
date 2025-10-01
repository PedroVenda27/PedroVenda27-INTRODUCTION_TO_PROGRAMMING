# 19) Escreva um programa que leia 10 números do utilizador e
# indique, no fim, quantos números são primos, quantos são pares e
# quantos são divisíveis por 3.
pares = 0
primos = 0
div3 = 0
x = 1


while x<=10:
    # Introdução de um número
    numero = int(input("Introduza um número: "))

    # Verifica se o número é divisivel por 2 (Par)
    if  numero % 2 == 0: # Se numero inserido a dividir por 2 dá resto 0
        pares = pares + 1 # contador de Pares (+1)
    
    # Verifica se o número é divisivel por 3
    if numero % 3 == 0: # Se numero inserido a dividir por 3 dá resto 0
        div3 = div3 + 1 # contador de Divisiveis por 3 (+1)

    # Verifica se o número é primo
    if numero > 1:
        for i in range(2, numero): # Se numero inserido a dividir por qualquer valor no intervalo de 2 a numero inserido -1 dá resto 0
            if numero % i == 0:   
                break # contador primos mantem o valor  
        else: # Se numero inserido a dividir por qualquer valor no intervalo de 2 a numero inserido -1 dá resto 0
            primos = primos + 1  # ontador primos (+1)
             
    x=x+1

print("Existem" , pares , "numeros pares") # Print texto ("Existem" ..... "numeros pares) e quantidades de numeros pares
print("Existem" , primos , "numeros primos") # Print texto ("Existem" ..... "numeros primos) e quantidades de numeros primos
print("Existem" , div3 , "numeros divisiveis por 3") # Print texto ("Existem" ..... "numeros divisiveis por 3) e quantidades de numeros div3