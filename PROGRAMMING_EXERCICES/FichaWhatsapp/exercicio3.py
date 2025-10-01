# Faça um Programa que leia 4 notas, mostre as notas e a média na tela
n = 1
notas = []

while n<=4:
    nota = int(input(f"Insira a {n}º nota: "))
    n= n + 1
    notas.append(nota)

media = sum(notas) / len(notas)

print("Media das Notas: " ,media)
