# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.


n=1
numeros = []


while n <= 10:
        numero = int(input(f" Insira o {n}º numero: "))
        if numero <= 0 :
            print("insira valores validos valido")
        else:
            quadrado = (numero * numero)
            numeros.append(quadrado)
            n = n + 1


soma_quadrados = sum(numeros)
print("Soma dos Quadrados" , soma_quadrados)