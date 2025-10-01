# Faça um Programa que peça as quatro notas de 10 alunos,
# calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0
alunos = 1
contador = 0
n = 1
notas = []

while alunos <= 10:
    n = 1
    notas = []
    while n <= 4:
        numero = int(input(f"ALUNO {alunos} Insira a {n}º nota: "))
        if numero < 0 or numero > 20 :
            print("insira um valor valido")
        else:
            notas.append(numero)
            n = n + 1

    media = sum(notas)/len(notas)

    
    if media >= 7:
        contador = contador + 1
    alunos = alunos + 1


print(contador)

