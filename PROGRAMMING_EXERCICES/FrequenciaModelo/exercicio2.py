

string = (input("insira a sua string: "))

lista = string.split()
print(lista)

numpalavras = len(lista)
print("A sua String tem", numpalavras, "palavras")

pesquisa = (input("Insira a palavra que deseja procurar na string: "))

# Flag para verificar se a palavra foi encontrada
encontrada = False

# Procurar a palavra na lista
for palavra in lista:
    if palavra == pesquisa:
        encontrada = True
        break

# Exibir o resultado com base em se a palavra foi encontrada ou não
if encontrada:
    print(f"A palavra '{pesquisa}' foi encontrada na string inserida.")
else:
    print(f"A palavra '{pesquisa}' não foi encontrada na string inserida.")

numA = string.count("a" or "A") # CONTA O NUMERO DE A
numE = string.count("e" or "E") # CONTA O NUMERO DE E
numI = string.count("i" or "I") # CONTA O NUMERO DE I
numO = string.count("o" or "O") # CONTA O NUMERO DE O
numU = string.count("u" or "U") # CONTA O NUMERO DE U

print("Existem" ,numA, "letra(s) A ao longo do Texto")
print("Existem" ,numE, "letra(s) E ao longo do Texto")
print("Existem" ,numI, "letra(s) I ao longo do Texto")
print("Existem" ,numO, "letra(s) O ao longo do Texto")
print("Existem" ,numU, "letra(s) U ao longo do Texto")

palavrascom_a = []
contcom_a = 0
for palavras in lista:
    if palavras.startswith("a" or "A"):
        contcom_a = contcom_a + 1
        palavrascom_a.append(palavras)



print("Numero de Palavras começadas com a letra A", contcom_a)
print(palavrascom_a)

palavrasordenadas = sorted(lista)
print("Palavras Ordenadas Alfabeticamente", palavrasordenadas)