# 14) Escreva um programa que verifique se todos os elementos de um
# determinado vetor existem noutro vetor.

vetor2 = []
vetor1 = []  # Vetor (lista) vazia
i1 = 0
i2 = 0
n1 = 0
n2 = 0



while True:
    n1 = int(input("Digite o número de valores que deseja inserir na 1ª lista: "))
    if n1 > 0:
        break
    else:
        print("Por favor, insira um número inteiro superior a 0.")

while i1 < n1:
    num = int(input(f"Digite o {i1 + 1}º valor inteiro: "))
    vetor1.append(num)
    i1 += 1

while True:
    n2 = int(input("Digite o número de valores que deseja inserir na 2ª lista: "))
    if n2 > 0:
        break
    else:
        print("Por favor, insira um número inteiro superior a 0.")

while i2 < n1:
    num = int(input(f"Digite o {i2 + 1}º valor inteiro: "))
    vetor2.append(num)
    i2 += 1


condicao = True

for x in range(0, n2):
    if vetor2[x] not in vetor1:
        condicao = False
        break

if condicao:
    print("Todos os elementos do vetor2 existem no vetor1")
else:
    print("Nem todos os elementos do vetor2 existem no vetor1")
