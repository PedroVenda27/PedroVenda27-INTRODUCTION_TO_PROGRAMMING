n=1
vetor1 = []
vetor2 = []
vetor3 = []
vetor4 = []
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

n=1
while n <= 10:
        numero = int(input(f" Insira o {n}º numero do vetor3: "))
        if numero <= 0 :
            print("insira valores validos valido")
        else:
            vetor3.append(numero)
            n = n + 1

for x in range (0,10):
     vetor4.append(vetor1[x])
     vetor4.append(vetor2[x])
     vetor4.append(vetor3[x])

print("Vetor1 , Vetor2 e Vetor3 intercalados: " ,vetor4)

