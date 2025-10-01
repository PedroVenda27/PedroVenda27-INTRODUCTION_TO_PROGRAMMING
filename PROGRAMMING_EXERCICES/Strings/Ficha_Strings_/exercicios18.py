# 18) Crie um programa que leia 10 nomes para um vector de strings e os ordene
# alfabeticamente na saída. 

# Inicializa a lista para armazenar os nomes
nomes = []

i = 0
while i < 10:
    nome = input(f"Introduza o {i+1}º nome: ")

    # Verifica se o nome contém apenas letras e espaços
    if nome.replace(" ", "").isalpha():
        nomes.append(nome) # adiciona o texto da variavel nome a variavel nomes
        i = i + 1
    else:
        print("Nome inválido. Por favor, introduza apenas letras e espaços.")

# Ordena a lista de nomes alfabeticamente
nomes.sort()

# Imprime os nomes ordenados
print("Nomes ordenados alfabeticamente:")
for nome in nomes:
    print(nome)
