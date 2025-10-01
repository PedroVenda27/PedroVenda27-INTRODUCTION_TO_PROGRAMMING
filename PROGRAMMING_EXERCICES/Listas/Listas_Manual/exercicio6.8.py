#PESQUIZA DE UM ELEMENTO


L = [15, 7, 27, 39]
p = int(input("Digite o 1º valor a procurar: "))
v = int(input("Digite o 2º valor a procurar: "))

x=0
while x<len(L):
    if L[x]==p:
       print(f"O valor {p} foi encontrado na lista.")
       break
    x=x+1
else:
   print(f"O valor {p} não foi encontrado na lista.")