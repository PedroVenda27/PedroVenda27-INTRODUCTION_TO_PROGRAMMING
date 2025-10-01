# 19) Crie um método para verificar se uma string é constituída apenas por algarismos.
# O método deverá retornar um valor booleano true neste caso.

# Solicita ao utilizador que introduza uma string
texto = input("Introduza uma string: ")

# Verifica se a string é composta apenas por algarismos
if texto.isdigit():
    print("A string é composta apenas por algarismos.")
    Value = True
else:
    print("A string não é composta apenas por algarismos.")
    value = False
