# 11) Crie um programa que leia um vetor de 10 inteiros. Os valores
# deverão estar no intervalo [0,100]. O programa não deverá aceitar
# valores fora deste intervalo. O programa deverá indicar a soma dos
# inteiros múltiplos de 5 existentes no vetor. 


vetor = []  # Vetor (lista) vazia
i = 0
n = 10

while i < n:
    num = int(input(f"Digite o {i + 1}º valor inteiro: "))
    if 0 <= num <= 100:
        vetor.append(num)
        i = i + 1
    else:
        print("Por favor, insira um número válido (O valor deve ser inteiro e estar compreendido entre 0 e 100)")

print("Vetor:", vetor)

multiplos_de_5=[]
soma_multiplos_de_5 = 0
for x in range(10):
    if vetor[x] % 5 == 0:
        soma_multiplos_de_5 += vetor[x]
        multiplos_de_5.append(vetor[x])

print("múltiplos de 5:", multiplos_de_5)
print("Soma dos múltiplos de 5:", soma_multiplos_de_5)
print("Fim do programa")