# 26) Crie um método que aceite 2 strings como argumentos e verifique se o
# comprimento da primeira string é superior ao da segunda. 


# Solicita ao utilizador que introduza a primeira string
string1 = input("Introduza a primeira string: ")

# Solicita ao utilizador que introduza a segunda string
string2 = input("Introduza a segunda string: ")

comp1 = len(string1)
comp2 = len(string2)

if comp1 > comp2:
    print(" o texto inroduzido na string 1 é maior que o da string 2")
else:
    print(" o texto inroduzido na string 1 não é maior que o da string 2")
