# 27) Crie um método que aceite 2 strings como argumentos e verifique se a segunda
# string é o inverso da primeira, ignorando as maiúsculas e minúsculas.

# Solicita ao utilizador que introduza a primeira string
string1 = input("Introduza a primeira string: ")

# Solicita ao utilizador que introduza a segunda string
string2 = input("Introduza a segunda string: ")

# Remove espaços em branco e converte para letras minúsculas (ou maiúsculas)
string1 = string1.replace(" ", "").lower()
string2 = string2.replace(" ", "").lower()

# Verifica se a segunda string é o inverso da primeira
if string1 == string2[::-1]:
    print("A segunda string é o inverso da primeira.")
else:
    print("A segunda string não é o inverso da primeira.")
