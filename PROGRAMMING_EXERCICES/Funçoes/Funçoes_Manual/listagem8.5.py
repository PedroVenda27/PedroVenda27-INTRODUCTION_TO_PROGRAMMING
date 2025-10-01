#8.5 PESQUIZA EM UMA LISTA DO PRIMEIRO LOCAL

def pesquizavalor(lista,valor):
    for x,e in enumerate(lista):
        if e == valor:
            return x
        
        
L = [1,2,3,4,5,1,2,3,4,5,1,2,3,4,56,4,4,3,7,]

print(pesquizavalor(L,4))

#8.5 PESQUIZA EM UMA LISTA DE TODOS OS LOCAIS


def pesquisavalor(lista, valor):
    indices = []
    for i, elemento in enumerate(lista):
        if elemento == valor:
            indices.append(i)
    return indices

L = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 56, 4, 4, 3, 7]

print(pesquisavalor(L, 4))