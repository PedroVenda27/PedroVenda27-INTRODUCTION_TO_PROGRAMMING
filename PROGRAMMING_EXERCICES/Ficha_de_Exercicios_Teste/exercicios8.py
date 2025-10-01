# 8) Escreva um programa em que o utilizador vai introduzindo as
# idades dos alunos de uma determinada turma até ser introduzido o
# número -1. No fim deverá indicar o número de alunos e a média de
# idades. O programa deverá garantir que apenas são introduzidos
# números positivos (com a exceção do -1 final).





Soma = 0
total = 0
trapp = 1
x = 0
while trapp<=1:
    idade = int(input("Insira o valor da idade:         Caso não tenha mais nenhuma idade a introduzir introduza o valor (-1)  "))

    if idade > 0 and idade < 130:
       x=x+1

    if  idade == -1:
      trapp = 2

    Soma=total+idade
    total=Soma
Soma = Soma+1

print("Soma dos Valores:",Soma)
media= Soma // x
print("Média de idades dos Alunos = %.2f: Anos" % media)
