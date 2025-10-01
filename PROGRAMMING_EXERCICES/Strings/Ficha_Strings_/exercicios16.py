# 16) Crie um programa que leia nomes do utilizador e termine quando for introduzido
# um nome repetido (ignorar maiúsculas e minúsculas).

# Inicializa uma string vazia para armazenar os nomes
nomes = ""

while True:
    # Solicita um nome ao utilizador
    nome = input("Introduza um nome: ").lower()

    # Verifica se o nome já foi introduzido
    if nome in nomes:
        print("Nome repetido! Programa terminado.")
        break
    else:
        # Adiciona o nome à string, com uma vírgula como separador
        nomes = nomes + nome + " "

print("Fim de Programa")

# Note que esta abordagem pode ter problemas se os nomes introduzidos contiverem vírgulas.