#PESQUIZA DE UM ELEMENTO


L = [15, 7, 27, 39]
p = int(input("Digite o 1º valor a procurar: "))
v = int(input("Digite o 2º valor a procurar: "))
achou = False


x=0
while x<len(L):
    if L[x]==p:
       achou = True
       print(f"O valor {p} foi encontrado na posição {x} da lista.")
    elif L[x]==v:
       achou = True
       print(f"O valor {v} foi  encontrado na posição {x} da lista.")
    x=x+1

if achou == False:
    print(f"Nenhum dos valores {p} e {v} foi encontrado na lista.")