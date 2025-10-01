# 22) Crie um programa que leia uma string e a imprima em maiúsculas, em
# minúsculas, em formato de título (as primeiras letras maiúsculas), em formato de
# frase (apenas a primeira letra maiúscula) e invertendo as maiúsculas e minúsculas.

# Solicita ao utilizador que introduza uma string
texto = input("Introduza uma string : ")

print( "Maiusculas: ", texto.upper())
print( "Minusculas: ", texto.lower())
print( "Titulo: ", texto.title())
print( "Frase: ", texto.capitalize())
print( "Troca Maiscula com minuscula e vice versa: ", texto.swapcase())
