#12 Escreva um programa que indique se todos os valores de um
# vetor são iguais, se são todos diferentes, ou se há valores
# repetidos no vetor. Para testar utilize um vetor cujo tamanho e
# valores inteiros são introduzidos pelo utilizador. 

vetor = []  # Vetor (lista) vazia
i = 0
n = 0

while True:
    n = int(input("Digite o número de valores que deseja inserir na lista: "))
    if n > 1:
        break
    else:
        print("Por favor, insira um número inteiro superior a 1.")

diferentes = False
valores_iguais = False

while i < n:
    num = int(input(f"Digite o {i + 1}º valor inteiro: "))
    vetor.append(num)
    i += 1

if not diferentes:
    print("Os valores são todos diferentes.")

if not valores_iguais:
    for x in range(1, n):
        if vetor[0] == vetor[x]:
            valores_iguais = True
        else:
            valores_iguais = False
            break

if valores_iguais:
    print("Os valores são todos iguais.")
else:
    print("Os valores não são todos iguais.")
