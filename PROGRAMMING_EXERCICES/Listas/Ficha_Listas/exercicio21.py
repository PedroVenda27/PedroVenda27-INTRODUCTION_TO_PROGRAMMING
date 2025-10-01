# 21) Escreva um programa para determinar o valor mais comum (moda)
# num vetor de inteiros. Teste com um vetor de 100 posições preenchido
# aleatoriamente com valores entre 0 e 10. 

import random

vetor = []
n=1
while n <= 100:
    valor = random.randint(0,10)
    vetor.append(valor)
    n=n+1
print(vetor)

contador = 0
maxcontador = 0

for num in vetor:
    for x in range(0,100):
        if num == vetor[x]:
            contador = contador + 1
    if contador > maxcontador:
        maxcontador = contador  
        moda = num

print("Moda dos Valores:" , moda)