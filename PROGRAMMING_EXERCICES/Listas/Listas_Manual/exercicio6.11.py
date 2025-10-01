

L=[]
for e in L:
    n=int(input("Digite um número (0 sai):"))
    if n == 0:
        break
    L.append(n)
x=0
for x in L:
    if x <len(L):
        print(L[x])
        x=x+1
        
# Não funciona com for uma vez que existe
# a possiblidade de a lista inicial ser uma lista vazia 