# 8) Crie um programa que, numa string substitua todas as letras “v” por “b” e todas
# as ocorrências de “ão” por “om”. 

texto = input("Introduza o texto: ")
texto = texto.strip()

# Substituir "v" por "b" e "ão" por "om"

texto = texto.lower().replace("v", "b")
texto = texto.lower().replace("ão", "om")

print(texto)
print (texto)
