# 10) Crie um programa que leia um nome de um utilizador e apresente apenas o
#primeiro e o último nome


# Solicita ao usuário que insira o nome completo
nomecompleto = input("Introduza o seu nome Completo: ")

# Divide o nome completo em uma lista de palavras usando o espaço como delimitador
palavras = nomecompleto.split()

# Obtém o primeiro nome (primeiro elemento da lista)
primeiro_nome = palavras[0]

# Obtém o último nome (último elemento da lista)
ultimo_nome = palavras[-1]

# Exibe o primeiro e o último nome
print("Primeiro e Ultimo Nome: ", primeiro_nome , ultimo_nome)
