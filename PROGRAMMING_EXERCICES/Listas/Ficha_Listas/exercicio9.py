# 9) Crie um programa que leia 10 números float, coloque-os num vetor
# e calcule a sua média.

vetor = []  # Vetor (lista) vazia
i = 0
n = 10

while i < n:
        num = int(input((f"Digite o {i + 1}º valor inteiro: ")))
        if num <0:
            print("Não é possivel colocar um numero negativo")
        else:
            vetor.append(num)
            i=i+1

print(vetor)
soma = sum(vetor)
media = soma/i
print("O valor da media é",media)
print("fim de Programa")