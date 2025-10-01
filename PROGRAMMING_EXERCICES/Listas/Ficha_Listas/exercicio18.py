# 18) Crie um programa para somar 2 vetores de tamanhos diferentes
# e colocar o resultado num 3º vetor.


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

soma2 = sum(vetor2)

print(vetor2)


# interpetação 1 
vetor3.append(soma1 + soma2)
print("Soma do Vetor 1 e 2:", vetor3)

# interpetação 2
vetor4 = vetor1 + vetor2
print("Soma do Vetor 1 e 2:", vetor4)


