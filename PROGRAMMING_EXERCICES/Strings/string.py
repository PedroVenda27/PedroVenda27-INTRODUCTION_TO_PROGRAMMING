# IMPRIME NA MESMA LINHA


s = "Ola Mundo!!"
print (s[0])
print (s[1])
print (s[2])

print (s[0:2]) # IMPRIME DE 0 A 1
print (s[1:3]) # IMPRIME DE 1 A 2
print (s[0:3]) # IMPRIME DE O A 2

print (s[1:]) # imprime da 1 até a ultima
print (s[:-1]) # imprime até a penultima letra

tam = len(s) # VÊ O TAMNHO / NUMERO DE CARACTERES
print (tam)
print(s[0:tam -1]) # IMPRIME DE O A PENULTIMO

for x in range (tam-1,-1,-1): # IMPRIME EM ORDEM INVERIDA
    print(s[x], end="") # IMPRIME NA MESMA LINHA

total_pontos = s.count("!") # CONTA O NUMERO DE PONTOS DE EXCLAMAÇÃO
print(total_pontos)

texto = "a2"

if texto.isdigit():
    print ("é um numero")
