
# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

texto = input("Introduza uma string : ")

texto = texto.replace("a" or "A","") 
texto = texto.replace("e" or "E","") 
texto = texto.replace("i" or "I","") 
texto = texto.replace("o" or "O","") 
texto = texto.replace("u" or "U","")
texto = texto.replace(" ","") 

consoantes = len(texto)
print(consoantes)