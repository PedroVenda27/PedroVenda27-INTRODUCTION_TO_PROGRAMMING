#13) Crie um programa para verificar se uma string é um palíndromo.


# Solicita ao utilizador que introduza uma string
texto = input("Introduza uma string para verificar se é um palíndromo: ")

# Remove espaços e converte para minúsculas
texto_limpo = texto.replace(" ", "").lower()

# Verifica se a string é igual à sua versão invertida
if texto_limpo == texto_limpo[::-1]:
    print("A string é um palíndromo.")
else:
    print("A string não é um palíndromo.")






