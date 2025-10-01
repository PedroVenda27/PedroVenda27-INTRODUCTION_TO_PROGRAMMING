# 19) Crie um programa para determinar o maior valor entre as
# posições de dois vetores e colocar o resultado num 3º vetor.

vetor3 = []
vetor1 = []
vetor2 = []
n=1

while True:
    valor = int(input(f"(insira 0 caso deseje terminar) Introduza o {n}º valor a colocar no vetor 1: "))
    if valor == 0:
        break
    if valor < 0:
        print("insira um valor inteiro positivo")
    if valor >= 1:
        vetor1.append(valor)
        n=n+1
soma1 = sum(vetor1)

print(vetor1)


n=1
while True:
    valor = int(input(f"(insira 0 caso deseje terminar) Introduza o {n}º valor a colocar no vetor 2: "))
    if valor == 0:
        break
    if valor < 0:
        print("insira um valor inteiro positivo")
    if valor >= 1:
        vetor2.append(valor)
        n=n+1




# Maior vetor 1      
maior1 = vetor1[0]

for num in vetor1:
    if num > maior1:
        maior1 = num


# Maior vetor 2   
maior2 = vetor2[0]

for num in vetor2:
    if num > maior2:
        maior2 = num

if maior1 > maior2:
    vetor3.append(maior1)
else:
    vetor3.append(maior2)


print("Maior valor comparando ambos os vetores", vetor3)