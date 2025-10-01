# 17) Crie um programa que indique qual de três strings introduzidas pelo utilizador
# tem um comprimento superior.

# Solicita ao utilizador que introduza uma string1
string1 = input("Introduza um texto para a string1: ")

# Solicita ao utilizador que introduza uma string2
string2 = input("Introduza um texto da string2: ")

# Solicita ao utilizador que introduza uma string3
string3 = input("Introduza um texto para a string3: ")

comp1 = len(string1)
comp2 = len(string2)
comp3 = len(string3)

if comp1 > comp2 and comp3:
    print("O Texto da string1 é o mais comprido")
if comp2 > comp1 and comp3:
    print("O Texto da string2 é o mais comprido")
if comp3 > comp2 and comp1:
    print("O Texto da string3 é o mais comprido")
else:
    print("Não é possivel determinar qual o maior")
    