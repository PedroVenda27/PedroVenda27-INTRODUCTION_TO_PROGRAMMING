#1) Escreva um programa que preencha um vetor de 100 posições com os
# primeiros 100 números pares.


pares = []
numero = 0
while len(pares) < 100:
    if numero % 2 == 0:
        pares.append(numero)
    numero +=1
print(pares)