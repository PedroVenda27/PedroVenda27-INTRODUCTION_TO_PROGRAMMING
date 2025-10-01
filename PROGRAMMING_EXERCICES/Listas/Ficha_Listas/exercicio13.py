# 13) Crie um programa que leia um vetor de inteiros cujo tamanho
# será introduzido pelo utilizador, tamanho esse que nunca será
# inferior a 5 ou superior a 25. O programa deverá indicar ao
# utilizador se o vetor é constituído (ou não) por valores pares e
# ímpares alternados. Exemplo: O vetor [1, 2, 5, 6, 3, 2] verifica
# esta condição.

vetor = []  # Vetor (lista) vazia
i = 0
n = 0


while True:
    n = int(input("Digite o número de valores que deseja inserir na lista: "))
    if n > 5 and n < 25:
        break
    else:
        print("Por favor, insira um número inteiro superior a 5 e inferior a 25.")

while i < n:
    num = int(input(f"Digite o {i + 1}º valor inteiro: "))
    vetor.append(num)
    i += 1

condicao = True

if (vetor[0] % 2 == 0):
    par=True
else:
    par=False

if par:
    for x in range(0,n-1,2):
        if (vetor[x] % 2 == 0):
            condicao = True
        else:
            condicao = False
            if condicao:
                for x in range(1,n-1,2):
                    if (vetor[x+1] % 2 != 0):
                        condicao = True
                    else:
                        condicao = False


if not par:
    for x in range(0,n-1,2):
        if (vetor[x] % 2 != 1):
            condicao = True
        else:
            condicao = False
            if condicao:
                for x in range(1,n-1,2):
                    if (vetor[x+1] % 2 == 0):
                        condicao = True
                    else:
                        condicao = False

if condicao:
    print("O vetor é constituído por valores pares e ímpares alternados")
else:
    print("O vetor não é constituído por valores pares e ímpares alternados")



