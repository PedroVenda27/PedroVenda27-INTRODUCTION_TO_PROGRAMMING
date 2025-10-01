#4) Crie um programa que apresente a soma de todos os valores de um
#vetor de inteiros de 10 posições. Os valores devem ser introduzidos
#pelo utilizador. 

vetor = []  #vetor (lista) vazia

# Solicitar os 10 valores
for i in range(10):
    valor = int(input(f"Digite o {i + 1}º valor inteiro: "))
    vetor.append(valor)

soma = sum(vetor)

print(f"A soma dos valores no vetor é: {soma}")