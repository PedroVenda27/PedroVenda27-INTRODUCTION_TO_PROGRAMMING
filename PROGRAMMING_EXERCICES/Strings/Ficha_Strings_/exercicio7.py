#7) Crie um programa que inverta uma string.

nome = input("Introduza o Nome: ")
nome = nome.strip()

tam = len(nome) # VÊ O TAMNHO / NUMERO DE CARACTERES
print (tam)

for x in range (tam-1,-1,-1): # IMPRIME EM ORDEM INVERIDA
    print(nome[x], end="") # IMPRIME NA MESMA LINHA
    