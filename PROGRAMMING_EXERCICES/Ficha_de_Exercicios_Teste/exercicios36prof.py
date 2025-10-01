# 36) Sequência de Padovan: Similar à sequência de Fibonacci, a
# sequência de Padovan é definida da seguinte forma: P(n) = P(n-2) +
# P(n-3) com os primeiros valores P(0) = 1, P(1) = 1, P(2) = 1.
# Escreva um programa que mostre os primeiros n termos da sequência
# de Padovan, sendo n fornecido pelo utilizador.

 
n = 0
while n <= 0:
    try:
        n = int(input("Quantos termos da seqeuência de Padovan deseja ver: "))
    except ValueError:
        print("Dados inválidos1")
 
serie_padovan = ""
p0 = p1 = p2 = 1
 
for x in range(n):
    if x < 3:
        if x == 0:
            serie_padovan += "1"
        else:
            serie_padovan += ", 1"
    else:
        padovan = p0 + p1
        serie_padovan += f", {padovan}"
        p0 = p1
        p1 = p2
        p2 = padovan
 
print(serie_padovan)