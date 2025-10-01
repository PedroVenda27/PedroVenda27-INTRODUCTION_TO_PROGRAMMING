# 10) Escreva um programa para ler as notas de n alunos (sendo n
# introduzido pelo utilizador). As notas deverão estar entre 1 e 5.
# O programa deverá contar quantos alunos tiveram cada uma das notas
# possíveis.

Nota1 = 0
Nota2 = 0
Nota3 = 0
Nota4 = 0
Nota5 = 0


n =0
n = int(input("Inroduza o número de Classificações a inserir"))
x=0
trapp=0
while trapp<=0:
    Nota = int(input("Inroduza a classificação do Aluno (1 a 5 apenas numeros inteiros)"))

    if Nota == 1:
     Nota1=Nota1+1
     x=x+1

    if Nota == 2:
     Nota2=Nota2+1
     x=x+1

    if Nota == 3:
     Nota3=Nota3+1
     x=x+1

    if Nota == 4:
     Nota4=Nota4+1
     x=x+1

    if Nota == 5:
     Nota5=Nota5+1
     x=x+1

    if Nota != 1 and Nota != 2 and Nota != 3 and Nota != 4 and Nota != 5:
        print("A Nota nao corresponde a um numero inteiro entre 1 e 5")

    if n == x:
      trapp = 1

print("Alunos com classificação 1:", Nota1)
print("Alunos com classificação 2:", Nota2)
print("Alunos com classificação 3:", Nota3)
print("Alunos com classificação 4:", Nota4)
print("Alunos com classificação 5;", Nota5)

