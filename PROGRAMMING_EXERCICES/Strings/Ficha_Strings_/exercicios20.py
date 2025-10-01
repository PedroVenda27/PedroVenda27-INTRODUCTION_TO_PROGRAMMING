# 20) Crie um método que receba uma string como argumento e retorne true se a
# string não contiver algarismos. 

# Solicita ao utilizador que introduza uma string
texto = input("Introduza uma string: ")

# Verifica se a string é composta apenas por algarismos
if texto.isalpha():
    print("A string não contem algarismos.")
    Value = "True"
    print(Value)
else:
    print("A string contem algarismos.")
    value = "False"
    print(value)
