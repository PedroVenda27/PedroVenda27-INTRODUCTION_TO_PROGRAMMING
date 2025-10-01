# 15) Escreva um programa que inverta a ordem dos elementos de um
# vetor de inteiros. Compare os resultados com a função reverse. 

vetor = [1, 2, 3, 4, 5, 6, 7, 8]
print("Inicial",vetor)
inicial = vetor

n = len(vetor)

for x in range(n // 2):
    auxiliar = vetor[x]
    vetor[x] = vetor[n - 1 - x]
    vetor[n - 1 - x] = auxiliar

print("Apos codigo",vetor)

vetor.reverse()
print("verificação com reverse", vetor , "=" , inicial )
