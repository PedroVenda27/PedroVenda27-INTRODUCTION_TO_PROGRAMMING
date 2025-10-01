#3) Escreva um programa em que 20 valores inteiros entre 1 e 10 são
#introduzidos pelo utilizador num vetor. Depois, o utilizador deverá
#indicar um valor e o programa deverá indicar em que posição ou
#posições, este valor existe no vetor. Se o valor não existir no
#vetor o programa deverá dar a respetiva mensagem.

# ler 20 valores inteiros entre 1 e 10
TAM = 20
v = []
n = 1

while n <= TAM:
    valor = int(input(f"Introduza o valor {n} de {TAM} (entre 1 e 10): "))
    if valor >= 1 and valor <= 10:
        v.append(valor)
        n += 1
    else:
        print("AVISO: Número fora dos limites pretendidos. Tente novamente!")

print(v)

# ler um numero entre 1 e 10 e pesquisar no vetor
resPesquisa = ""
while True:
    valorPesquisa = int(input(f"Indique o valor que deseja pesquisar (entre 1 e 10): "))
    if valorPesquisa >= 1 and valorPesquisa <= 10:
        for x, num in enumerate(v):
            if num == valorPesquisa:
                if resPesquisa == "":
                    resPesquisa += str(x + 1)
                else:
                    resPesquisa += ", " + str(x + 1)
        break
    else:
        print("AVISO: Número fora dos limites pretendidos. Tente novamente!")


# mostrar os resultados no ecrã
if resPesquisa == "":
    print(f"O valor {valorPesquisa} Não foi encontrado no vetor")
else:
    print(f"O valor {valorPesquisa} foi encontrado na posição {resPesquisa} do vetor")







