#ADIÇÃO DE ELEMENTOS A UMA LISTA

lista1=[]
while True:
    n=int(input("Digite um número (0 sai):"))
    if n == 0:
        break
    lista1.append(n)
x=0
while x < len(lista1):
    print(lista1[x])
    x=x+1