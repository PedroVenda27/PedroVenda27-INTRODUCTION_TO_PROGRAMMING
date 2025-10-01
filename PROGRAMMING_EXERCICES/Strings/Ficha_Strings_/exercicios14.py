#14) Escreva um programa que indique quantas vezes surge cada vogal numa string.

# Solicita ao utilizador que introduza uma string
texto = input("Introduza uma string para verificar se é um palíndromo: ")

numA = texto.count("a" or "A") # CONTA O NUMERO DE A
numE = texto.count("e" or "E") # CONTA O NUMERO DE E
numI = texto.count("i" or "I") # CONTA O NUMERO DE I
numO = texto.count("o" or "O") # CONTA O NUMERO DE O
numU = texto.count("u" or "U") # CONTA O NUMERO DE U

print("Existem" ,numA, "letra(s) A ao longo do Texto")
print("Existem" ,numE, "letra(s) E ao longo do Texto")
print("Existem" ,numI, "letra(s) I ao longo do Texto")
print("Existem" ,numO, "letra(s) O ao longo do Texto")
print("Existem" ,numU, "letra(s) U ao longo do Texto")

vogais=(numA + numE + numI + numO + numU)

print("Existem no total" ,vogais, "Vogais")