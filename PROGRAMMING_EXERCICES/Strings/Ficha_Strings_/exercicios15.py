# 15) Escreva um programa para determinar quantas vezes uma substring existe numa
# string.


# Solicita ao utilizador que introduza uma string
string = input("Introduza uma string: ")
# Solicita ao utilizador que introduza uma substring
substring = input("Introduza uma substring: ")

substringcount = string.count(substring) # CONTA O NUMERO DE A


print("A substring",substring,"esta presente" ,substringcount, "vezes na string")
