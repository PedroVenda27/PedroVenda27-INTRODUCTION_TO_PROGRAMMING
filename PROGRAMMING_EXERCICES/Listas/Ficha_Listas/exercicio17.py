# 17) Escreva um programa que peça as idades de 32 alunos de uma
# turma. O programa deve guardar estes valores num vetor e no final
# indicar a idade máxima, mínima média e moda da turma.

vetor = []
n=1
while n <= 30:
    valor = int(input(f"(insira 0 caso deseje terminar) Introduza a idade do {n}º individuo: "))
    if valor <= 0:
        print("insira um valor inteiro positivo")
    if valor >= 1:
        vetor.append(valor)
        n=n+1

# Maior das idades       
maior = vetor[0]

for num in vetor:
    if num > maior:
        maior = num

print("maior idade"(maior))

# Menor das idades
menor = vetor[0]
for num in vetor:
   if num < menor:
      menor = num

print("menor idade"(menor))

# Média de idades
media = sum(vetor) / len(vetor)

print("Média de idades:"(media))

# Moda de idades

contador = 0
maxcontador = 0

for num in vetor:
    for x in range(0,30):
        if num == vetor[x]:
            contador = contador + 1
    if contador > maxcontador:
        maxcontador = contador 
        moda = num

print("Moda de idades:"(moda))

