# Faça um Programa que leia dois vetores com 10 elementos cada. 
# Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

n=1
vetor1 = []
vetor2 = []
vetor3 = []
while n <= 10:
        numero = int(input(f" Insira o {n}º numero do vetor1: "))
        if numero <= 0 :
            print("insira valores validos valido")
        else:
            vetor1.append(numero)
            n = n + 1

n=1
while n <= 10:
        numero = int(input(f" Insira o {n}º numero do vetor2: "))
        if numero <= 0 :
            print("insira valores validos valido")
        else:
            vetor2.append(numero)
            n = n + 1

for x in range (0,10):
     vetor3.append(vetor1[x])
     vetor3.append(vetor2[x])

print("Vetor1 e Vetor2 intercalados: " ,vetor3)

