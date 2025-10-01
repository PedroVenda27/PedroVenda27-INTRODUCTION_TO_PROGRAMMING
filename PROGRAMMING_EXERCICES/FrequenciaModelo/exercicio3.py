string = (input("insira a sua string: "))

lista = string.split()
for palavra in lista:
    print(palavra)


numpalavras = len(lista)
print("Numero de Palavras da Lista", numpalavras)

print("Lista Normal",lista)

lista.reverse()

print("Lista Invertida",lista)

