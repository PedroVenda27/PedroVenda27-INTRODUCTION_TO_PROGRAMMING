# Moda de idades
vetor = []
n=1
while n <= 30:
    valor = int(input(f"(insira 0 caso deseje terminar) Introduza a idade do {n}º individuo: "))
    if valor <= 0:
        print("insira um valor inteiro positivo")
    if valor >= 1:
        vetor.append(valor)
        n=n+1

contador = 0
maxcontador = 0

for num in vetor:
    for x in range(0,30):
        if num == vetor[x]:
            contador = contador + 1
    if contador > maxcontador:
        maxcontador = contador 
        moda = num

print(moda)