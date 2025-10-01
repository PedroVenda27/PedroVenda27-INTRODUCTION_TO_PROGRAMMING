#PESQUIZA USSANDO FOR
L = [7, 9, 10, 12]
p = int(input("Digite o valor a procurar: "))
for e in L:
    if e == p:
        print("Elemento Encontrado!")
        break
else:
    print("Elemento não foi encontrado :( ")
