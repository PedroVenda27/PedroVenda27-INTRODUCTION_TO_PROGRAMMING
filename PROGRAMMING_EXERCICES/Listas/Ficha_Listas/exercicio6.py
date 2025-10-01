

vetor = []  # Vetor (lista) vazia
i = 0
n = 10

while i < n:
    inserir= True
    num = int(input((f"Digite o {i + 1}º valor inteiro: ")))
    if i != 0:
        for x in range (0,i):
            if vetor[x] == num:
                inserir  = False
                break

    if inserir:
        vetor.append(num)
        i += 1

print(vetor)
