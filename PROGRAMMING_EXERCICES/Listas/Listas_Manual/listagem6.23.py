#PESQUIZA DE UM ELEMENTO


L = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar: "))
achou = False

x=0
while x<len(L):
    if L[x]==p:
       achou = True
       break  # Se o valor foi encontrado, não é necessário continuar procurando
    x=x+1

# Verificar se o valor foi encontrado
if achou:
    print(f"O valor {p} foi encontrado na lista.")
else:
    print(f"O valor {p} não foi encontrado na lista.")