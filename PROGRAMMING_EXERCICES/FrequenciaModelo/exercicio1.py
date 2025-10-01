import random


lista = []
while len(lista) <= 10:
    numero = random.randint(0,100)
    print(numero)
    lista.append(numero)

maior = lista[0]
for i, num in enumerate(lista):
    if num > maior:
        maior = num
        posicao = i

print("Maior Valor" ,maior,"Posição no indice" ,posicao )


def media_numeros(lista):
    return sum(lista) / len(lista)

print("Media dos numeros:",media_numeros(lista))

def dobro_lista(lista):
    return [num * 2 for num in lista]

print("Lista multiplicada por 2: ",dobro_lista(lista))