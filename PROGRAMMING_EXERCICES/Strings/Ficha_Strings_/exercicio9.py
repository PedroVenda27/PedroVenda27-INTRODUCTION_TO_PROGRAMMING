# 9) Crie um programa que remova todas as ocorrências de uma substring dentro de
#uma string.


texto = input("Introduza o texto: ")
texto = texto.strip()
substring = input("Introduza a substring a ser removida: ")

# Usando a função replace para substituir todas as ocorrências da substring por uma string vazia
novotexto = texto.lower().replace(substring.lower(), '').lower()

print("Texto original:", texto)
print("Texto após remover a substring:", novotexto)
