#2) Escreva um programa que procure e indique o maior valor (e a
# respetiva posição) de um vetor de 10 posições introduzido pelo
# utilizador

numeros = []

for i in range(10):
    n = int(input(f"Introduza um número para o vetor {i}: "))
    numeros.append(n)

maior = max(numeros)
posicao = numeros.index(maior)

print(f"O maior elemento é {maior} e está na posição{posicao}.")



