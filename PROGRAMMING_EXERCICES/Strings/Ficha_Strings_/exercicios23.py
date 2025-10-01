#23) Crie métodos que aceitem uma string como argumento e retornem:
#a. O número de ocorrências da letra ‘a’.
#b. O número de vogais.
#c. O valor true se a string for um palíndromo.

# Solicita ao utilizador que introduza uma string
texto = input("Introduza uma string : ")

numA = texto.count("a" or "A") # CONTA O NUMERO DE A
numE = texto.count("e" or "E") # CONTA O NUMERO DE E
numI = texto.count("i" or "I") # CONTA O NUMERO DE I
numO = texto.count("o" or "O") # CONTA O NUMERO DE O
numU = texto.count("u" or "U") # CONTA O NUMERO DE U

print(" a) Existem" ,numA, "letra(s) A ao longo do Texto")

vogais=(numA + numE + numI + numO + numU)

print(" b) Existem no total" ,vogais, "Vogais")

# Remove espaços e converte para minúsculas
texto_limpo = texto.replace(" ", "").lower()

# Verifica se a string é igual à sua versão invertida
if texto_limpo == texto_limpo[::-1]:
    print(" c) A string é um palíndromo.")
else:
    print(" c) A string não é um palíndromo.")
