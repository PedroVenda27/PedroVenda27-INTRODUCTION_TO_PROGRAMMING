#5) Escreva um programa que determine o 2º maior valor de um vetor.


vetor = []  #vetor (lista) vazia
maior = 0
segundomaior = 0

# Solicitar os 10 valores
for i in range(10):
    valor = int(input(f"Digite o {i + 1}º valor inteiro: "))
    vetor.append(valor)

for t in vetor:
        if vetor[t] > maior:
            maior = vetor[t]
            posição = t
vetor.remove(maior)

for h in vetor:
        if vetor[h] > segundomaior:
            segundomaior = vetor[h]

print("O segundo maior valor é:",segundomaior)
