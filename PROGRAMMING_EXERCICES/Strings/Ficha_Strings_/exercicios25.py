# 25) Crie um método que receba duas strings como argumentos e retorne um valor
# booleano de acordo com as seguintes especificações:
# a. true se todos os caracteres da primeira string existirem na 2ª string. O
# número de ocorrências não é importante.
# b. false em caso contrário

# Solicita ao utilizador que introduza a primeira string
string1 = input("Introduza a primeira string: ")

# Solicita ao utilizador que introduza a segunda string
string2 = input("Introduza a segunda string: ")

# Inicializa uma variável para verificar se todos os caracteres estão presentes
todos_presentes = True

# Verifica se todos os caracteres da primeira string existem na segunda string
for caractere in string1:
    if caractere not in string2:
        todos_presentes = False
        break

# Imprime o resultado
if todos_presentes:
    print("Todos os caracteres da primeira string existem na segunda string.")
else:
    print("Pelo menos um caractere da primeira string não existe na segunda string.")